# Lightweight AI for Disaster Response (Offline + Energy Efficient)

def classify_disaster(alert_text):
    alert_text = alert_text.lower()

    # Simple keyword-based rules
    if "earthquake" in alert_text or "tremor" in alert_text:
        return "Earthquake"
    elif "flood" in alert_text or "water level" in alert_text:
        return "Flood"
    elif "fire" in alert_text or "wildfire" in alert_text or "burning" in alert_text:
        return "Wildfire"
    elif "drought" in alert_text or "dry" in alert_text:
        return "Drought"
    elif "tsunami" in alert_text or "wave" in alert_text:
        return "Tsunami"
    elif "storm" in alert_text or "cyclone" in alert_text:
        return "Storm"
    else:
        return "Unknown / Other"

# Response prioritization logic
def get_response_action(disaster_type):
    responses = {
        "Earthquake": "Evacuate buildings, check for aftershocks.",
        "Flood": "Move to higher ground, avoid flooded roads.",
        "Wildfire": "Evacuate area, inform fire department.",
        "Drought": "Conserve water, provide aid to farmers.",
        "Tsunami": "Evacuate coastal areas immediately.",
        "Storm": "Seek shelter, secure loose items.",
        "Unknown / Other": "Assess situation, report to emergency services."
    }
    return responses.get(disaster_type, "No response available.")

# Example usage
if __name__ == "__main__":
    alert = input("Enter disaster alert message: ")
    disaster_type = classify_disaster(alert)
    action = get_response_action(disaster_type)
    
    print("\nPredicted Disaster Type:", disaster_type)
    print("Recommended Action:", action)
