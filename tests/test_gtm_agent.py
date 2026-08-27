import os
import unittest

os.environ.setdefault("OPENAI_API_KEY", "test-key")
from gtm_agent.gtm_agent import send_prospect_email


class SendProspectEmailTests(unittest.TestCase):
    def test_disqualified_prospect_is_blocked_without_message_id(self):
        result = send_prospect_email.func(
            {
                "prospect_id": "LEAD-50002",
                "name": "Liam O'Brien",
                "email": "liam.obrien@meridiansystems.com",
            },
            "Scheduling a Technical Deep Dive",
            "Please let me know your availability.",
            runtime=None,
            from_rep={"email": "rep@example.com", "name": "Rep"},
        )

        self.assertEqual(result["status"], "blocked")
        self.assertNotIn("message_id", result)


if __name__ == "__main__":
    unittest.main()
