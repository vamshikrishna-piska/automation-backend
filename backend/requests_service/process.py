def process_request(payload):
    return {
        "summary": payload,
        "field_count": len(payload)
    }
