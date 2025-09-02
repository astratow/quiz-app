mkdir -p src/{views,store,utils}
echo "Foldery views, store i utils stworzone"
touch src/main.ts
touch src/views/{Home.vue,Quiz.vue,Results.vue}
touch src/components/{QuestionCard.vue,AnswerButton,QuestionExplanation.vue,QuestionFactory.vue}
mkdir -p src/store
touch src/store/quiz.ts
mkdir -p src/utils
touch src/utils/{useTimer.ts,shuffle.ts,checkAnswer.ts}
echo "✅ Struktura Vue Quiz App została utworzona!"