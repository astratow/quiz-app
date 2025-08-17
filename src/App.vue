<script setup lang="ts">
import { ref } from "vue";
import Question from "./components/Question.vue";
import questions from "./data/questions.json";

interface QuestionData {
  text: string;
  answers: string[];
  correct: string;
  explanation: string;
}

const score = ref(0);
const index = ref(0);
const answered = ref(false);
const currentQuestion = ref<QuestionData | null>(questions[0]);

function handleAnswer(correct: boolean) {
  answered.value = true;
  if (correct) score.value++;
}

function nextQuestion() {
  index.value++;
  answered.value = false;
  if (index.value < questions.length) {
    currentQuestion.value = questions[index.value];
  } else {
    currentQuestion.value = null;
    alert(`Quiz finished! Final score: ${score.value}/${questions.length}`);
  }
}

</script>

<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-6">
    <h1 class="text-2xl font-bold mb-6">Verbal Reasoning Quiz</h1>

    <Question
      v-if="currentQuestion"
      :question="currentQuestion"
      @answered="handleAnswer"
    />

    <div class="mt-6">
      <p class="font-semibold">Score: {{ score }}</p>
    </div>

    <button
      v-if="answered"
      @click="nextQuestion"
      class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
    >
      Next
    </button>
  </div>
</template>
