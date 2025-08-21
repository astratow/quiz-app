export interface Option {
    label: string;
    value: string;
}

export interface Question {
    type: string;
    text: string[];
    options: Option[];
    correct: string;
    explanation: string;
}

export interface Example extends Question {}

export interface QuestionSet {
    id: string;
    instruction: string;
    example: Example;
    questions: Question[];
}