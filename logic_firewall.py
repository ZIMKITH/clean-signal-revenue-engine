import functions_framework

@functions_framework.http
def governance_check(request):
    """
    Serverless Logic Firewall for Zensar Demo.
    - Input: JSON payload from n8n
    - Output: JSON with Governance Decision (CLEAN vs QUARANTINE)
    """
    
    # 1. Parse the Incoming JSON
    request_json = request.get_json(silent=True)
    if not request_json:
        return ({"error": "No JSON provided"}, 400)

    # 2. Define Risk Rules (The "Banned" List)
    RISK_ROOTS = ['bankrupt', 'fraud', 'investigat', 'litigat', 'sanction', 'insolven', 'scam']

    # 3. Extract & Normalize Data
    company = request_json.get('company_name', 'Unknown')
    # Combine fields to catch risks hidden in descriptions or news
    full_text = (f"{company} {request_json.get('description', '')} {request_json.get('news_summary', '')}").lower()

    # 4. Execute Deterministic Logic
    risk_detected = False
    risk_reason = "Passed Logic Firewall"

    for root in RISK_ROOTS:
        if root in full_text:
            risk_detected = True
            risk_reason = f"QUARANTINE: Found risk signal '{root}'"
            break

    # 5. Return Structured Response
    return ({
        "processed_company": company,
        "firewall_status": "QUARANTINE" if risk_detected else "CLEAN",
        "firewall_reason": risk_reason,
        "governance_layer": "GCP-Serverless-Python-v1"
    }, 200)
