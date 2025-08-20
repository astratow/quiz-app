<template>
  <div class="text-center max-w-2xl mx-auto">
    <div class="mb-8">
      <h1 class="text-4xl font-bold text-gray-800 mb-4">Verbal Reasoning Quiz</h1>
      <p class="text-xl text-gray-600 mb-2">
        Train your logical thinking and text analysis skills
      </p>
      <p class="text-gray-500">
        Prepare for exams: SAT, GMAT, A-levels, UKCAT, GRE
      </p>
    </div>
    <div class="flex flex-col md:flex-row gap-8 mb-8">
      <button
        class="flex-1 px-8 py-6 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-semibold text-2xl"
        @click="selectMode('practice')"
      >
        Practice Mode
      </button>
      <button
        class="flex-1 px-8 py-6 bg-green-600 text-white rounded-lg hover:bg-green-700 font-semibold text-2xl"
        @click="selectMode('timed')"
      >
        Timed Quiz
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits<{ (e: 'mode-selected', mode: 'practice' | 'timed'): void }>();

function selectMode(mode: 'practice' | 'timed') {
  emit('mode-selected', mode);
}
</script>
