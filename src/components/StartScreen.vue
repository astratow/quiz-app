<template>
  <div class="text-center max-w-2xl mx-auto">
    <div class="mb-8">
      <h1 class="text-4xl font-bold text-gray-800 mb-4">Verbal Reasoning Quiz</h1>
      <p class="text-xl text-gray-600 mb-2">
        Train your logical thinking and text analysis skills
      </p>
      <p class="text-gray-500">
        Prepare for exams.
      </p>
    </div>

    <div class="grid gap-4 md:grid-cols-2 mb-8">
      <!-- Practice Mode -->
      <div class="bg-white rounded-xl shadow-lg p-6 border-2 border-transparent hover:border-blue-500 transition-all cursor-pointer"
           @click="selectMode('practice')">
        <div class="text-4xl mb-4">📚</div>
        <h3 class="text-xl font-semibold mb-2">Practice Mode</h3>
        <p class="text-gray-600 mb-4">
          Solve questions at your own pace without time pressure. 
          Perfect for learning and exploring different question types.
        </p>
        <div class="text-sm text-blue-600 font-medium">
          ✓ No time limit<br>
          ✓ Instant feedback<br>
          ✓ Answer explanations
        </div>
      </div>

      <!-- Timed Quiz Mode -->
      <div class="bg-white rounded-xl shadow-lg p-6 border-2 border-transparent hover:border-green-500 transition-all cursor-pointer"
           @click="selectMode('timed')">
        <div class="text-4xl mb-4">⏱️</div>
        <h3 class="text-xl font-semibold mb-2">Timed Quiz</h3>
        <p class="text-gray-600 mb-4">
          Test yourself under exam conditions. 
          Limited time for each question.
        </p>
        <div class="text-sm text-green-600 font-medium">
          ✓ 90 seconds per question<br>
          ✓ Exam simulation<br>
          ✓ Time tracking
        </div>
      </div>
    </div>

    <div class="bg-gray-50 rounded-lg p-4 mb-6">
      <h4 class="font-semibold text-gray-700 mb-2">📊 Your Statistics</h4>
      <div class="grid grid-cols-3 gap-4 text-center">
        <div>
          <div class="text-2xl font-bold text-blue-600">{{ stats.totalQuestions }}</div>
          <div class="text-sm text-gray-600">Questions solved</div>
        </div>
        <div>
          <div class="text-2xl font-bold text-green-600">{{ stats.correctAnswers }}</div>
          <div class="text-sm text-gray-600">Correct answers</div>
        </div>
        <div>
          <div class="text-2xl font-bold text-purple-600">{{ stats.accuracy }}%</div>
          <div class="text-sm text-gray-600">Accuracy</div>
        </div>
      </div>
    </div>

    <div class="text-sm text-gray-500">
      💡 Tip: Start with practice mode to get familiar with the question format
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';


interface Stats {
  totalQuestions: number;
  correctAnswers: number;
  accuracy: number;
}

const emit = defineEmits<{
  (e: 'mode-selected', mode: 'practice' | 'timed'): void;
}>();

// Mock stats - in a real app, these would come from localStorage or a backend
const stats = computed<Stats>(() => {
  const total = 0; // Would be loaded from localStorage
  const correct = 0; // Would be loaded from localStorage
  
  return {
    totalQuestions: total,
    correctAnswers: correct,
    accuracy: total > 0 ? Math.round((correct / total) * 100) : 0
  };
});

function selectMode(mode: 'practice' | 'timed') {
  emit('mode-selected', mode);
}
</script>

