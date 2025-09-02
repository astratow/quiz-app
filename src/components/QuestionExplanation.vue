<template>
    <div class="mt-4 text-sm text-gray-600">
        <p v-if="selected === correct" class="text-green-600 font-semibold">✅ Correct!</p>
    </div>
</template>
<script setup lang="ts">
const props = defineProps<{
    selected: string | null;
    correct: string;
}>();
</script>