<script setup lang="ts">
import { ref, computed } from "vue";
import Question from "./components/Question.vue";
import groups from "./data/quest.json";
import StartScreen from "./components/StartScreen.vue";
import AnswerModal from "./components/AnswerModal.vue";
import type { QuestionSet, Question as QuizQuestion } from "./types/quiz";

// Use only the JSON data
const questionSets = groups as QuestionSet[];
const currentSet = ref<QuestionSet>(questionSets[0]);

// App state
const currentScreen = ref<'start' | 'quiz' | 'results'>('start');
const gameMode = ref<'practice' | 'timed' | null>(null);
const score = ref(0);
const index = ref(0);
const answered = ref(false);
const selectedAnswer = ref<string | null>(null);
const timeLeft = ref(90);
const timeInterval = ref<number | null>(null);

const questions = computed(() => currentSet.value.questions);
const currentQuestion = computed<QuizQuestion|undefined>(() => questions.value[index.value]);

function handleModeSelected(mode: 'practice' | 'timed') {
  gameMode.value = mode;
  currentScreen.value = 'quiz';
  score.value = 0;
  index.value = 0;
  answered.value = false;
  selectedAnswer.value = null;
  if (mode === 'timed') {
    startTimer();
  }
}

function startTimer() {
  timeLeft.value = 90;
  timeInterval.value = setInterval(() => {
    timeLeft.value--;
    if (timeLeft.value <= 0) {
      handleTimeOut();
    }
  }, 1000);
}

function clearTimer() {
  if (timeInterval.value) {
    clearInterval(timeInterval.value);
    timeInterval.value = null;
  }
}

function handleTimeOut() {
  clearTimer();
  answered.value = true;
  selectedAnswer.value = null;
}

function handleAnswer(answer: string) {
  answered.value = true;
  selectedAnswer.value = answer;
  if (gameMode.value === 'timed') {
    clearTimer();
  }
  if (currentQuestion.value && answer === currentQuestion.value.correct) {
    score.value++;
  }
}

function nextQuestion() {
  if (index.value >= questions.value.length - 1) {
    currentScreen.value = 'results';
    clearTimer();
    return;
  }
  index.value++;
  answered.value = false;
  selectedAnswer.value = null;
  if (gameMode.value === 'timed') {
    startTimer();
  }
}

function restartQuiz() {
  currentScreen.value = 'start';
  clearTimer();
}

const isTimedMode = computed(() => gameMode.value === 'timed');
const timeDisplay = computed(() => {
  const minutes = Math.floor(timeLeft.value / 60);
  const seconds = timeLeft.value % 60;
  return `${minutes}:${seconds.toString().padStart(2, '0')}`;
});

</script>

<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Start Screen: Mode Selection -->
    <StartScreen v-if="currentScreen === 'start'" @mode-selected="handleModeSelected" />
    <!-- Quiz Screen -->
    <div v-else-if="currentScreen === 'quiz'" class="min-h-screen flex flex-col items-center justify-center p-6">
      <!-- Back to Menu Button -->
      <button
        @click="restartQuiz"
        class="mb-6 px-4 py-2 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 font-semibold self-start"
      >
        ← Back to Menu
      </button>
      <!-- Header with title and timer -->
      <div class="w-full max-w-4xl mb-6">
        <div class="flex justify-between items-center mb-4">
          <h1 class="text-2xl font-bold text-gray-800">
            {{ gameMode === 'practice' ? 'Practice Mode' : 'Timed Quiz' }}
          </h1>
          <div v-if="isTimedMode" class="text-right">
            <div class="text-2xl font-bold" :class="timeLeft <= 15 ? 'text-red-600' : 'text-blue-600'">
              {{ timeDisplay }}
            </div>
            <div class="text-sm text-gray-600">Time remaining</div>
          </div>
        </div>
        <!-- Progress bar -->
        <div class="w-full bg-gray-200 rounded-full h-2 mb-4">
          <div 
            class="bg-blue-600 h-2 rounded-full transition-all duration-300" 
            :style="{ width: `${((index + 1) / questions.length) * 100}%` }"
          ></div>
        </div>
      </div>
      <!-- Instruction always visible -->
      <div class="w-full max-w-2xl mb-6">
        <div class="bg-white rounded-xl shadow p-6 mb-4">
          <h2 class="text-xl font-bold mb-2">Instructions</h2>
          <p class="whitespace-pre-line">{{ currentSet.instruction }}</p>
        </div>
      </div>
      <!-- Question Component -->
      <Question
        v-if="currentQuestion"
        :question="currentQuestion"
        :answered="answered"
        :selectedAnswer="selectedAnswer"
        @answered="handleAnswer"
      />
      <div v-else class="text-center">
        <p class="text-red-600 font-semibold">No questions available!</p>
      </div>
      <!-- Score and Modal -->
      <div class="mt-6">
        <p class="font-semibold">Score: {{ score }}</p>
      </div>
      <AnswerModal 
        :visible="answered"
        :is-correct="selectedAnswer === currentQuestion?.correct"
        :explanation="currentQuestion?.explanation || ''"
        :is-last="index + 1 >= questions.length"
        @next="nextQuestion"
      />
    </div>
    <!-- Results Screen -->
    <div v-else-if="currentScreen === 'results'" class="min-h-screen flex items-center justify-center p-6">
      <div class="text-center max-w-2xl mx-auto">
        <div class="mb-8">
          <h1 class="text-4xl font-bold text-gray-800 mb-4">🎉 Quiz Complete!</h1>
          <p class="text-xl text-gray-600">
            {{ gameMode === 'practice' ? 'Practice Mode' : 'Timed Quiz' }}
          </p>
        </div>
        <div class="bg-white rounded-xl shadow-lg p-8 mb-8">
          <div class="grid grid-cols-3 gap-6 mb-6">
            <div class="text-center">
              <div class="text-3xl font-bold text-blue-600">{{ score }}</div>
              <div class="text-sm text-gray-600">Correct answers</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-gray-600">{{ questions.length }}</div>
              <div class="text-sm text-gray-600">Total questions</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-green-600">{{ Math.round((score / questions.length) * 100) }}%</div>
              <div class="text-sm text-gray-600">Accuracy</div>
            </div>
          </div>
          <div class="text-lg mb-4">
            <span v-if="(score / questions.length) >= 0.8" class="text-green-600 font-semibold">
              🌟 Excellent! You have outstanding verbal reasoning skills.
            </span>
            <span v-else-if="(score / questions.length) >= 0.6" class="text-blue-600 font-semibold">
              👍 Good job! Keep practicing to improve even further.
            </span>
            <span v-else class="text-orange-600 font-semibold">
              💪 Don't worry! More practice will help you achieve better results.
            </span>
          </div>
        </div>
        <div class="space-y-4">
          <button
            @click="restartQuiz"
            class="w-full px-6 py-3 bg-gray-600 text-white rounded-lg hover:bg-gray-700 font-semibold"
          >
            Back to Menu
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
