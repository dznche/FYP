import numpy as np
import nltk

class SubjectiveTestGenerator:
    def __init__(self, summary, num_questions):
        self.summary = summary
        self.num_questions = num_questions
        self.question_patterns = [
            "Explain in detail ",
            "Define ",
            "What do you mean by ",
            "Explain the significance of  "
        ]

    def generate_test(self):
        sentences = nltk.sent_tokenize(self.summary)
        questions = []

        for _ in range(self.num_questions):
            sentence = np.random.choice(sentences)
            tokens = nltk.word_tokenize(sentence)
            tagged_words = nltk.pos_tag(tokens)

            # Filter nouns and noun phrases
            nouns = [word for word, pos in tagged_words if pos.startswith('NN')]

            if nouns:
                question_pattern = np.random.choice(self.question_patterns)
                noun = np.random.choice(nouns)
                question = f"{question_pattern}{noun}?"
                questions.append({"Question": question, "Answer": sentence})

        return questions

if __name__ == "__main__":
    summary_text = """
    Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence
    concerned with the interactions between computers and human language, in particular how to program computers
    to process and analyze large amounts of natural language data.
    """

    generator = SubjectiveTestGenerator(summary_text, num_questions=5)
    test_questions = generator.generate_test()

    print("Generated Test Questions:")
    for idx, question in enumerate(test_questions, 1):
        print(f"Question {idx}: {question['Question']}")
       
