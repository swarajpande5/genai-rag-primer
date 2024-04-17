def make_prompt(query: str) -> str:
    prompt = ("""QUESTION: '{query}'
ANSWER:
""").format(query=query)

    return prompt


def make_rag_prompt(query: str, relevant_passage: str) -> str:
    relevant_passage_escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = ("""You are a helpful and informative bot that answers questions. \
You may use text from the reference passage included below.
If the passage is irrelevant to the \
question or the answer, you may ignore using the passage.

**Reference Passage:**

{relevant_passage}

QUESTION: '{query}'
ANSWER:
""").format(query=query, relevant_passage=relevant_passage_escaped)

    return prompt
