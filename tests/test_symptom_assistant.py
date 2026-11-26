import unittest

from symptom_assistant import RULES, analyse_symptoms, normalise_symptoms


class SymptomAssistantTests(unittest.TestCase):
    def test_xml_knowledge_base_loads_definitions_and_categories(self):
        self.assertGreaterEqual(len(RULES), 5)
        cold = next(rule for rule in RULES if rule.name == "Common cold")
        self.assertIn("Viral", cold.category)
        self.assertIn("viral infection", cold.definition.lower())

    def test_normalise_symptoms(self):
        self.assertEqual(
            normalise_symptoms(" Cough, FEVER ,, sore throat "),
            {"cough", "fever", "sore throat"},
        )

    def test_red_flag_is_prioritised(self):
        result = analyse_symptoms({"cough", "chest pain"})
        self.assertIn("URGENT", result)
        self.assertIn("999", result)

    def test_flu_like_rule_matches(self):
        result = analyse_symptoms({"fever", "body aches", "cough"})
        self.assertIn("Flu-like illness", result)
        self.assertIn("not a diagnosis", result.lower())

    def test_hay_fever_rule_matches(self):
        result = analyse_symptoms({"sneezing", "itchy eyes"})
        self.assertIn("hay fever", result.lower())

    def test_unknown_symptoms_are_not_reassuring(self):
        result = analyse_symptoms({"unlisted symptom"})
        self.assertIn("does not mean nothing is wrong", result)


if __name__ == "__main__":
    unittest.main()
