# Decision logic

## Approach

This artefact demonstrates a **top-down, rule-based AI system**. The illness
knowledge is stored separately in the `illnesses.xml` file. The Python program
loads that XML file, compares the user's symptom phrases with its predefined
symptom keywords, and displays possible explanations.

## XML knowledge base

Each `<illness>` entry contains:
- an ID;
- a display name;
- a cautious description;
- a list of symptom phrases.

To add another example, create another `<illness>` entry in `illnesses.xml`.
Add its name, description and symptom keywords. The XML file must remain valid.

## Processing flow

1. Read comma-separated symptom phrases.
2. Convert phrases to lowercase and remove extra spaces.
3. Load illness names, descriptions and symptom keywords from `illnesses.xml`.
4. Check the small red-flag keyword list first.
5. If a red-flag phrase is present, show the urgent safety message.
6. Otherwise compare the symptoms with each XML rule.
7. Rank matching rules by the number of matching keywords.
8. Display up to three possible explanations and explain the limitations.

## Example

Input: `fever, body aches, cough`

The flu-like illness entry contains all three phrases, so it is returned as a
possible explanation. This is a keyword overlap demonstration, not a
probability or clinical confidence score.

## Limitations and safety

- This is a coursework demonstration, not a diagnostic tool or medical device.
- The XML examples and emergency keyword list are deliberately incomplete.
- A missing match does not mean the user is healthy.
- A keyword match cannot confirm a condition; symptoms can have many causes.
- The program does not collect medical history, age, medication, duration, or severity.
- Never use this prototype to rule out an emergency or delay professional care.
- In England, contact NHS 111 for urgent advice when it is not an emergency.
  Call 999 for a medical emergency.
