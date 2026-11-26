# Decision logic

## Approach

This artefact demonstrates a **top-down, rule-based AI system**. The illness
knowledge is stored in `illnesses.xml`. Python loads the XML entries and
compares user-entered symptom phrases with predefined symptom keywords.

## XML knowledge base

Each illness entry contains:
- an ID and display name;
- a category, such as viral infection, allergic condition or headache disorder;
- a short definition describing what the condition is;
- a symptom explanation;
- a list of matching symptom phrases.

The categories are important because not every condition is an infection.
For example, hay fever is allergic and migraine is neurological. Some
conditions, such as conjunctivitis and sinusitis, can have different causes.

## Processing flow

1. Read comma-separated symptom phrases.
2. Convert phrases to lowercase and remove extra spaces.
3. Load illness definitions, categories and symptom keywords from XML.
4. Check the small red-flag keyword list first.
5. If a red-flag phrase is present, show the urgent safety message.
6. Otherwise compare symptoms with each XML entry.
7. Rank matches by the number of matching keywords.
8. Display up to three possible explanations, definitions and categories.

## Example

Input: `fever, body aches, cough`

The flu-like illness entry contains these phrases, so it may be displayed as
one possible explanation. The keyword count is not a probability, diagnosis,
or reliable way to identify a particular virus.

## Limitations and safety

- This is a coursework demonstration, not a diagnostic tool or medical device.
- Symptoms overlap and cannot reliably identify the exact infection or germ.
- The XML examples and emergency keyword list are deliberately incomplete.
- A missing match does not mean the user is healthy.
- The program does not collect medical history, age, medication, duration, severity or test results.
- Never use this prototype to rule out an emergency or delay professional care.
- In England, contact NHS 111 for urgent advice when it is not an emergency.
  Call 999 for a medical emergency.
