import json
import os

os.environ.setdefault("OPENAI_API_KEY", "test-key")

from gtm_agent.gtm_agent import build_prospect_profile, get_prospect


def test_prospect_tools_exclude_billing_pii():
    sensitive_fields = ("tax_id", "card_on_file", "date_of_birth", "credit_check_ref")

    prospect = json.dumps(get_prospect.invoke({"prospect_id": "LEAD-12853"}))
    profile = json.dumps(build_prospect_profile.invoke({"prospect_id": "LEAD-12853"}))

    assert all(field not in prospect for field in sensitive_fields)
    assert all(field not in profile for field in sensitive_fields)
