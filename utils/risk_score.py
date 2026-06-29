import streamlit as st

def calculate_risk_score(
    lead_time,
    deposit_type,
    previous_cancellations,
    repeated_guest,
    special_requests,
):

    score = 0

    # Lead Time
    if lead_time > 180:
        score += 35
    elif lead_time > 100:
        score += 25
    elif lead_time > 50:
        score += 15

    # Deposit
    if deposit_type == "No Deposit":
        score += 25
    elif deposit_type == "Refundable":
        score += 10

    # Previous cancellations
    if previous_cancellations >= 2:
        score += 25
    elif previous_cancellations == 1:
        score += 15

    # Repeat guest
    if repeated_guest == 0:
        score += 10

    # Special requests
    if special_requests == 0:
        score += 5

    return min(score, 100)