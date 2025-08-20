<script setup lang="ts">
import { ref, computed } from "vue";
import Question from "./components/Question.vue";
import groups from "./data/questions.json";

interface QuestionData {
  type?: string;
  text: string | string[];
  options?: string[];
  optionLetters?: string[];
  answers?: string[];
  correct: string | string[];
  explanation: string;
}

interface ExampleData {
  text: string[];
  options: string[];
  optionLetters: string[];
  correct: string;
  explanation: string;
}

interface QuestionGroup {
  id: string;
  instruction: string;
  example: ExampleData;
  questions: QuestionData[];
}

type GameMode = 'practice' | 'timed';
type AppScreen = 'start' | 'group-info' | 'quiz' | 'results';

const currentScreen = ref<AppScreen>('start');
const gameMode = ref<GameMode>('practice');
const score = ref(0);
const index = ref(0);
const answered = ref(false);
const selectedAnswer = ref<string | null>(null);
const currentQuestion = ref<QuestionData | null>(null);
const timeLeft = ref(90); // seconds for timed mode
const timeInterval = ref<number | null>(null);

const selectedGroupIdx = ref<number | null>(null);
const selectedGroup = computed(() =>
  selectedGroupIdx.value !== null ? (groups as QuestionGroup[])[selectedGroupIdx.value] : null
);
const questions = computed(() => selectedGroup.value ? selectedGroup.value.questions : []);

function selectGroup(idx: number) {
  selectedGroupIdx.value = idx;
  currentScreen.value = 'group-info';
}

function startGame(mode: GameMode) {
  gameMode.value = mode;
  currentScreen.value = 'quiz';
  score.value = 0;
  index.value = 0;
  answered.value = false;
  selectedAnswer.value = null;
  currentQuestion.value = questions.value.length > 0 ? questions.value[0] : null;
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
  selectedAnswer.value = null; // No answer selected
  setTimeout(() => {
    nextQuestion();
  }, 2000);
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
    currentQuestion.value = null;
    clearTimer();
    return;
  }
  index.value++;
  answered.value = false;
  selectedAnswer.value = null;
  currentQuestion.value = questions.value[index.value];
  if (gameMode.value === 'timed') {
    startTimer();
  }
}

function restartQuiz() {
  currentScreen.value = 'start';
  clearTimer();
  selectedGroupIdx.value = null;
}

function goToGroupInfo() {
  currentScreen.value = 'group-info';
  index.value = 0;
  answered.value = false;
  selectedAnswer.value = null;
  currentQuestion.value = null;
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
    <!-- Start Screen: Group Selection -->
    <div v-if="currentScreen === 'start'" class="min-h-screen flex flex-col items-center justify-center p-6">
      <h1 class="text-3xl font-bold mb-8">Select Question Set</h1>
      <div class="grid gap-6 w-full max-w-xl">
        <button
          v-for="(group, idx) in groups"
          :key="group.id"
          @click="selectGroup(idx)"
          class="p-6 bg-white rounded-xl shadow hover:bg-blue-50 border-2 border-transparent hover:border-blue-400 text-left text-lg font-semibold transition-all"
        >
          {{ group.instruction.substring(0, 80) }}<span v-if="group.instruction.length > 80">...</span>
        </button>
      </div>
    </div>

    <!-- Group Info Screen: Show instruction and example -->
    <div v-else-if="currentScreen === 'group-info' && selectedGroup" class="min-h-screen flex flex-col items-center justify-center p-6">
      <div class="bg-white rounded-xl shadow-lg p-8 max-w-2xl w-full mb-8">
        <h2 class="text-2xl font-bold mb-4">Instructions</h2>
        <p class="mb-6 whitespace-pre-line">{{ selectedGroup.instruction }}</p>
        <h3 class="text-xl font-semibold mb-2">Example</h3>
        <div class="mb-2">
          <div v-for="(frag, idx) in selectedGroup.example.text" :key="idx" class="mb-1">{{ frag }}</div>
        </div>
        <div class="mb-2 flex flex-wrap gap-2">
          <span v-for="(opt, idx) in selectedGroup.example.options" :key="opt" class="inline-block px-3 py-1 bg-gray-200 rounded">{{ opt }}: {{ selectedGroup.example.optionLetters[idx] }}</span>
        </div>
        <div class="mb-2"><strong>Answer:</strong> {{ selectedGroup.example.correct }}</div>
        <div class="text-gray-600 text-sm">{{ selectedGroup.example.explanation }}</div>
      </div>
      <div class="flex gap-4">
        <button @click="currentScreen = 'start'" class="px-6 py-3 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 font-semibold">Back</button>
        <button @click="startGame('practice')" class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-semibold">Start Practice</button>
        <button @click="startGame('timed')" class="px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 font-semibold">Start Timed</button>
      </div>
    </div>

    <!-- Quiz Screen -->
    <div v-else-if="currentScreen === 'quiz' && selectedGroup" class="min-h-screen flex flex-col items-center justify-center p-6">
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
      <!-- Question Component -->
      <Question
        v-if="currentQuestion"
        :question="currentQuestion"
        :answered="answered"
        :selected-answer="selectedAnswer"
        @answered="handleAnswer"
      />
      <div v-else-if="questions.length === 0" class="text-center">
        <p class="text-red-600 font-semibold">No questions available!</p>
      </div>
      <!-- Show current progress during quiz -->
      <div v-if="currentQuestion" class="mt-6 text-center">
        <p class="font-semibold">Score: {{ score }}/{{ questions.length }}</p>
        <p class="text-sm text-gray-600">Question {{ index + 1 }} of {{ questions.length }}</p>
        <!-- Timeout message for timed mode -->
        <div v-if="isTimedMode && answered && !selectedAnswer" class="mt-2">
          <p class="text-red-600 font-semibold">⏰ Time's up!</p>
        </div>
      </div>
      <!-- Next button -->
      <button
        v-if="answered && currentQuestion"
        @click="nextQuestion"
        class="mt-4 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-semibold"
      >
        {{ index + 1 >= questions.length ? 'View Results' : 'Next Question' }}
      </button>
    </div>

    <!-- Results Screen -->
    <div v-else-if="currentScreen === 'results' && selectedGroup" class="min-h-screen flex items-center justify-center p-6">
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
            @click="goToGroupInfo"
            class="w-full px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-semibold"
          >
            Try Again
          </button>
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
