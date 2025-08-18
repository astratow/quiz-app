# Verbal Reasoning Quiz App

An educational web app for training verbal reasoning skills through interactive quizzes. Built with **Vue 3**, **TypeScript**, **Vite**, and **Tailwind CSS**.

## Features
- 🧠 **Practice Mode**: Solve questions at your own pace, with instant feedback and answer explanations.
- ⏱️ **Timed Quiz**: Simulate exam conditions with a timer for each question.
- 📊 **Results & Feedback**: Get a summary of your score, accuracy, and detailed explanations after each quiz.
- 🗂️ **Question Bank**: Questions are stored locally in JSON for easy extension.
- 🎯 **Progress Tracking**: (Planned) Track your stats and progress over time.

## Who is it for?
- Students preparing for exams like SAT, GMAT, A-levels, UKCAT, GRE.
- Anyone wanting to improve logical reading and inference skills.

## Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (v16+ recommended)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)

### Setup
```bash
npm install
npm run dev
```
Then open [http://localhost:5173](http://localhost:5173) in your browser.

## Project Structure
- `src/components/` — Vue components (Quiz, StartScreen, etc.)
- `src/data/questions.json` — Question bank (edit or extend as needed)
- `src/App.vue` — Main app logic and routing
- `src/style.css` — Tailwind CSS styles

## Tech Stack
- [Vue 3](https://vuejs.org/) (Composition API)
- [TypeScript](https://www.typescriptlang.org/)
- [Vite](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)

## Roadmap
- [x] Practice and Timed modes
- [x] Local question bank
- [x] Results summary
- [ ] User stats and progress
- [ ] More question types
- [ ] Online deployment (Netlify/GitHub Pages)

## License
MIT
