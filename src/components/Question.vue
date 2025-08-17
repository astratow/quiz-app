<template>
    <div class="p-6 bg-white rounded-2xl shadow-md w-full max-w-xl">
        <h2 class="text-xl font-bold mb-4">{{ question.text }}</h2>
        <ul>
            <li v-for="(answer, idx) in question.answers" :key="idx" class="mb-2">
                <button
                    @click="selectAnswer(answer)"
                    class="w-full p-2 rounded-lg border hover:bg-gray-100 disabled:opacity-50"
                    :disabled="answered"
                >
                    {{ answer }}
                </button></li>
        </ul>
        <div v-if="answered" class="mt-4">
            <p v-if="isCorrect" class="text-green-600 font-semibold">✅ Correct!</p>
            <p v-else class="text-red-600 font-semibold">❌ Wrong!</p>
            <p  class="text-sm text-gray-600 mt-1">{{ question.explanation }}</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

interface QuestionData {
  text: string;
  answers: string[];
  correct: string;
  explanation: string;
}

const props = defineProps<{ question: QuestionData }>();
const emit = defineEmits<{
  (e: 'answered', correct: boolean): void
}>();

const answered = ref(false);
const isCorrect = ref(false);

function selectAnswer(answer: string) {
    answered.value = true;
    isCorrect.value = answer === props.question.correct;
    emit("answered", isCorrect.value);
}
</script>