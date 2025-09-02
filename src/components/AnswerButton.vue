<script setup lang="ts">
const props = defineProps<{
    option: { label: string; vaule: string };
    answered: boolean;
    selected: string | null;
    correct: string;
}>();
</script>
<template>
    <button
        @click="$emit('click')"
        :disabled="answered"
        class="-full p-3 rounded-lg border flex items-center hover:bg-gray-100 transition disabled:opacity-50"
        :class="{
            'bg-green-100 border-green-500': answered && option.value === correct,
            'bg-red-100 border-red-500': answered && option.value === selected && selected !== correct
    }"
    >
        <span class="font-bold mr-2">{{  option.label }}</span>
        <span>{{  option.value }}</span>
    </button>
</template>