<script setup lang="ts">
import { ref, computed } from "vue";

interface QuestionData {
    type?: string;
    text: string | string[];
    options?: string[];
    optionLetters?: string[];
    answers?: string[];
    correct: string | string[];
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

const isSameLetterMC = computed(() => props.question.type === 'same-letter-mc');
const isOldMC = computed(() => !props.question.type && Array.isArray(props.question.answers));

</script>
<template>
    <div class="p-6 bg-white rounded-2xl shadow-md w-full max-w-xl">
        <!-- same-letter-mc type -->
        <template v-if="isSameLetterMC">
            <h2 class="text-xl font-bold mb-4">
                <span v-for="(frag, idx) in question.text" :key="idx">
                    <span v-if="idx > 0"> &amp; </span>{{ frag }}
                </span>
            </h2>
            <ul>
                <li v-for="(letter, idx) in question.optionLetters" :key="idx" class="mb-2">
                    <button
                        @click="selectAnswer(letter)"
                        class="w-full p-2 rounded-lg border hover:bg-gray-100 disabled:opacity-50 flex items-center"
                        :class="{
                            'bg-green-100 border-green-500': answered && letter === question.correct,
                            'bg-red-100 border-red-500': answered && letter === selectedAnswer && letter !== question.correct,
                            'border-gray-300': !answered
                        }"
                        :disabled="answered"
                    >
                        <span class="font-bold mr-2">{{ question.options ? question.options[idx] : String.fromCharCode(65 + idx) }}</span>
                        <span>{{ letter }}</span>
                    </button>
                </li>
            </ul>
            <div v-if="answered" class="mt-4">
                <p v-if="selectedAnswer === question.correct" class="text-green-600 font-semibold">✅ Correct!</p>
                <p v-else class="text-red-600 font-semibold">❌ Wrong!</p>
                <p class="text-sm text-gray-600 mt-1">{{ question.explanation }}</p>
            </div>
        </template>

        <!-- Old format multiple choice -->
        <template v-else-if="isOldMC">
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
                    </button>
                </li>
            </ul>
            <div v-if="answered" class="mt-4">
                <p v-if="selectedAnswer === question.correct" class="text-green-600 font-semibold">✅ Correct!</p>
                <p v-else class="text-red-600 font-semibold">❌ Wrong!</p>
                <p class="text-sm text-gray-600 mt-1">{{ question.explanation }}</p>
            </div>
        </template>

        <!-- Fallback for unknown type -->
        <template v-else>
            <h2 class="text-xl font-bold mb-4">Unsupported question type</h2>
        </template>
    </div>
</template>
