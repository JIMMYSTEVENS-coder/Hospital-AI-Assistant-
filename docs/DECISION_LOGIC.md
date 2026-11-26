# Decision logic

## Approach

This artefact demonstrates a **top-down, rule-based AI system**. The developer
defines the knowledge in advance as condition rules. The program compares the
user's symptom phrases with those rules and produces possible explanations.

## Processing flow

1. Read comma-separated symptom phrases.
2. Convert phrases to lowercase and remove extra spaces.
3. Check the small red-flag keyword list first.
4. If a red-flag phrase is present, show the urgent safety message.
5. Otherwise compare the symptoms with each predefined rule.
6. Rank matching rules by the number of matching keywords.
7. Display up to three possible explanations and explain the limitations.

## Example

Input: `fever, body aches, cough`

The flu-like rule contains all three phrases, so it is returned as a possible
explanation. This is a keyword overlap demonstration, not a probability or
clinical confidence score.

## Limitations and safety

- This is a coursework demonstration, not a diagnostic tool or medical device.
- The rules and emergency keyword list are deliberately small and incomplete.
- A missing match does not mean the user is healthy.
- A keyword match cannot confirm a condition; symptoms can have many causes.
- The program does not collect medical history, age, medication, duration, or severity.
- Never use this prototype to rule out an emergency or delay professional care.
- In England, contact NHS 111 for urgent advice when it is not an emergency.
  Call 999 for a medical emergency.
