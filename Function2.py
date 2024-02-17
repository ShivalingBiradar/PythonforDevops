
# Keywords arguments
def vac_feedback(vac,efficacy):
    print(f"{vac} Vaccine is having {efficacy} % efficay.")
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effective, needs more trail.")

    elif (efficacy > 75 ) and (efficacy < 90 ):
        print("Can consider this vaccine.")

    elif efficacy >= 90:
        print("Sure, will take the shot.")

    else:
        print("Needs many more trails.")

vac_feedback("Pfizer", 95)
vac_feedback("Unknown", 45)
vac_feedback(efficacy=34, vac="Unknown")