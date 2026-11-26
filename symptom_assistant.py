"""Educational, XML-driven rule-based symptom assistant.

This program is a coursework demonstration, not a medical device or diagnostic
service. Its keyword rules are incomplete and must never be used to rule out
an emergency or decide whether professional care is needed.
"""
from dataclasses import dataclass
from pathlib import Path
import xml.etree.ElementTree as ET


@dataclass
class ConditionRule:
    name: str
    symptoms: set[str]
    explanation: str


def load_rules(xml_path: Path | None = None) -> list[ConditionRule]:
    """Load illness names, symptom keywords and explanations from illnesses.xml."""
    path = xml_path or Path(__file__).with_name("illnesses.xml")
    try:
        root = ET.parse(path).getroot()
    except (FileNotFoundError, ET.ParseError) as error:
        raise RuntimeError(f"Could not load the illness knowledge base: {error}") from error

    rules = []
    for illness in root.findall("illness"):
        name = illness.findtext("name", default="Unknown condition").strip()
        explanation = illness.findtext("description", default="No description available.").strip()
        symptoms = {
            item.text.strip().lower()
            for item in illness.findall("./symptoms/symptom")
            if item.text and item.text.strip()
        }
        if symptoms:
            rules.append(ConditionRule(name, symptoms, explanation))
    return rules


# The illness knowledge is stored separately in illnesses.xml.
RULES = load_rules()

# This deliberately small teaching list is NOT a complete emergency checklist.
RED_FLAGS = {
    "severe difficulty breathing",
    "chest pain",
    "blue lips",
    "unconscious",
    "severe bleeding",
    "signs of stroke",
}


def normalise_symptoms(text: str) -> set[str]:
    """Convert comma-separated symptom text into a set of normalised phrases."""
    return {part.strip().lower() for part in text.split(",") if part.strip()}


def analyse_symptoms(symptoms: set[str]) -> str:
    """Compare user phrases with the rules loaded from the XML knowledge base."""
    urgent = symptoms.intersection(RED_FLAGS)
    if urgent:
        return (
            "URGENT: You entered a symptom from this prototype's limited red-flag "
            "list. Call 999 now if you may be experiencing a medical emergency. "
            "This list is incomplete; do not rely on this program to assess emergencies."
        )

    matches = []
    for rule in RULES:
        overlap = symptoms.intersection(rule.symptoms)
        if overlap:
            matches.append((len(overlap), rule, sorted(overlap)))

    if not matches:
        return (
            "I cannot find a matching example rule for those symptoms. This does "
            "not mean nothing is wrong. For advice in England, use NHS 111 or contact "
            "a healthcare professional if you are concerned."
        )

    matches.sort(key=lambda item: item[0], reverse=True)
    lines = ["Possible explanations (not a diagnosis):"]
    for score, rule, overlap in matches[:3]:
        lines.append(f"- {rule.name}: {rule.explanation}")
        lines.append(f"  Matching keywords: {', '.join(overlap)}")
    lines.append(
        "The number of matching keywords is only a simple demonstration score; "
        "it is not a probability, medical confidence score, or diagnosis."
    )
    lines.append(
        "If you are worried or need urgent medical advice in England, contact NHS 111. "
        "Call 999 for a medical emergency."
    )
    return "\n".join(lines)


def main() -> None:
    print("Hospital Symptom Assistant — educational prototype only")
    print(f"Loaded {len(RULES)} example illness rules from illnesses.xml.")
    print("Enter symptoms separated by commas (for example: cough, fever).")
    print("Type 'quit' to exit. This is not a diagnostic tool.")
    while True:
        answer = input("\nYour symptoms: ").strip()
        if answer.lower() in {"quit", "exit"}:
            print("Goodbye. If you are concerned about your health, seek professional advice.")
            break
        symptoms = normalise_symptoms(answer)
        if not symptoms:
            print("Please enter at least one symptom.")
            continue
        print(analyse_symptoms(symptoms))


if __name__ == "__main__":
    main()
