# Hospital AI Assistant

A small Python coursework project demonstrating a **top-down, rule-based AI**
that compares user-entered symptom phrases with a set of predefined rules.

> **Important:** This is an educational prototype, not a medical device or
> diagnostic service. It cannot diagnose conditions, assess all emergencies,
> or replace professional medical advice. Its symptom rules and red-flag list
> are incomplete. Never use it to rule out an emergency or delay care.

## Features

- Accepts comma-separated symptom phrases.
- Normalises input by removing extra spaces and using lowercase.
- Checks a small red-flag keyword list before other rules.
- Compares symptoms with predefined example rules.
- Displays up to three possible explanations.
- Includes automated unit tests and decision-logic documentation.

## Requirements

- Python 3.10 or later (uses standard-library modules only).

## Run the assistant

```bash
python symptom_assistant.py
```

Enter symptoms separated by commas, for example:

```text
fever, body aches, cough
```

Type `quit` to exit.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Example behaviour

For `fever, body aches, cough`, the program can show **Flu-like illness** as
one possible explanation because those phrases match its predefined rule.
The keyword count is a simple demonstration score, not a probability or
clinical confidence score.

## Health and safety

If you are in England and need urgent medical advice that is not an emergency,
contact NHS 111. Call 999 for a medical emergency. The prototype's red-flag
keyword list is deliberately tiny and incomplete; it must not be relied on
for emergency assessment.

## Project documentation

- [Decision logic](docs/DECISION_LOGIC.md)
- [Testing guide](docs/TESTING.md)

## Project status

This is a basic rule-based starting example for an AI programming assignment.
An LLM integration may be explored separately, but it must not be presented as
a substitute for qualified clinical assessment.
