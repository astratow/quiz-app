<script setup lang="ts">
import { computed } from "vue";
import type { Question } from "../types/quiz";

const props = defineProps<{
    question: Question;
    answered: boolean;
    selectedAnswer: string | null;
}>();

const emit = defineEmits<{
    (e: 'answered', answer: string): void
}>();

function selectAnswer(answer: string) {
   if (!props.answered) {
        emit("answered", answer);
   }
}

const optionList = computed(() => props.question.options);
</script>
<template>
    <div class="p-6 bg-white rounded-2xl shadow-md w-full max-w-xl">
        <!-- same-letter-mc type -->
        <template v-if="question.type === 'same-letter-mc'">
            <h2 class="text-xl font-bold mb-4">
                <span v-for="(fragment, idx) in question.text" :key="idx">
                    <span v-if="idx > 0"> &amp; </span>{{ fragment }}
                </span>
            </h2>
            <ul>
                <li  v-for="option in optionList"
                    :key="option.label"
                    class="mb-2"
                    >
                    <button
                        @click="selectAnswer(option.value)"
                        class="w-full p-3 rounded-lg border flex  items-center
                                hover:bg-gray-100 transition disabled:opacity-50"
                        :disabled="answered"
                        :class="{
              'bg-green-100 border-green-500': answered && option.value === question.correct,
              'bg-red-100 border-red-500': answered && option.value === selectedAnswer && selectedAnswer !== question.correct,
            }"
                    >
                        <span class="font-bold mr-2">{{ option.label }}</span>
                        <span>{{ option.value }}</span>
                    </button>
                </li>
            </ul>

        </template>

        <!-- Old format multiple choice -->
        <!-- <template v-else-if="isOldMC">
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
        </template> -->

        <!-- Fallback for unknown type -->
        <template v-else>
            <h2 class="text-xl font-bold mb-4">Unsupported question type</h2>
        </template>
    </div>
</template>
