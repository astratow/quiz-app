<script setup lang="ts">
defineProps<{
    visible: boolean
    isCorrect: boolean
    explanation: string
    isLast: boolean
}>()

defineEmits<{ (e: 'next') : void }>()
</script>
<template>
  <div v-if="visible" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
    <div class="bg-white rounded-2xl shadow-lg p-8 max-w-md w-full text-center">
      <h2 
        class="text-2xl font-bold mb-4" 
        :class="isCorrect ? 'text-green-600' : 'text-red-600'"
      >
        {{ isCorrect ? "✅ Correct!" : "❌ Wrong!" }}
      </h2>
      <p class="text-gray-700 mb-6">{{ explanation }}</p>
      <button
        @click="$emit('next')"
        class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-semibold"
      >
        {{ isLast ? "View Results" : "Next Question" }}
      </button>
    </div>
  </div>
</template>