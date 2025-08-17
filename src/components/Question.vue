<script setup lang="ts">
import { ref } from "vue";

interface QuestionData {
    text: string;
    answers: string[];
    correct: string;
    explanation: string;
}

const props = defineProps<{ 
    question: QuestionData;
    answered: boolean;
    selectedAnswer: string | null;
}>();

const emit = defineEmits<{
    (e: 'answered', answer: string): void
}>();

function selectAnswer(answer: string) {
    emit("answered", answer);
}
</script>
<template>
    <div class="p-6 bg-white rounded-2xl shadow-md w-full max-w-xl">
        <h2 class="text-xl font-bold mb-4">{{ question.text }}</h2>
        <ul>
            <li v-for="(answer, idx) in question.answers" :key="idx" class="mb-2">
                <button
                    @click="selectAnswer(answer)"
                    class="w-full p-2 rounded-lg border hover:bg-gray-100 disabled:opacity-50"
                    :class="{
                        'bg-green-100 border-green-500': answered && answer === question.correct,
                        'bg-red-100 border-red-500': answered && answer === selectedAnswer && answer !== question.correct,
                        'border-gray-300': !answered
                    }"
                    :disabled="answered"
                >
                    {{ answer }}
                </button></li>
        </ul>
        <div v-if="answered" class="mt-4">
            <p v-if="selectedAnswer === question.correct" class="text-green-600 font-semibold">✅ Correct!</p>
            <p v-else class="text-red-600 font-semibold">❌ Wrong!</p>
            <p class="text-sm text-gray-600 mt-1">{{ question.explanation }}</p>
        </div>
    </div>
</template>
