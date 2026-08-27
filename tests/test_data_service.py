import unittest

from gtm_agent import data_service


class UpdateProspectInfoTests(unittest.TestCase):
    def test_update_prospect_info_persists_technology_and_invalidates_profile(self):
        prospect_id = "LEAD-71001"
        original_tech_stack = list(data_service.PROSPECTS[prospect_id]["tech_stack"])
        data_service._PROFILES[prospect_id] = {
            "prospect_id": prospect_id,
            "tech_stack": original_tech_stack,
        }

        try:
            result = data_service.update_prospect_info(prospect_id, "Kafka")

            self.assertIn("Kafka", data_service.fetch_tech_stack(prospect_id))
            self.assertTrue(result["persisted"])
            self.assertIn("Kafka", result["tech_stack"])
            profile = data_service.get_profile_from_db(prospect_id)["prospect_profile"]
            self.assertTrue(profile is None or "Kafka" in profile["tech_stack"])
        finally:
            data_service.PROSPECTS[prospect_id]["tech_stack"] = original_tech_stack
            data_service._PROFILES.pop(prospect_id, None)


if __name__ == "__main__":
    unittest.main()
