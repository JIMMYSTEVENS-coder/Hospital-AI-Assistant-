# Testing

Run the tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

Run the assistant:

```bash
python symptom_assistant.py
```

## Manual examples

| Input | Expected behaviour |
|---|---|
| `fever, body aches, cough` | Shows flu-like illness as a possible explanation |
| `sneezing, itchy eyes` | Shows possible hay fever |
| `chest pain` | Shows the urgent safety message |
| `unlisted symptom` | Says no example rule matched and does not reassure the user |
| blank input | Asks the user to enter at least one symptom |

The red-flag examples are only a tiny demonstration list and are not a complete
medical triage checklist.
