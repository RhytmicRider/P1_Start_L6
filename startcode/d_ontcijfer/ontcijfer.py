def ontcijfer(bericht, sleutel):
    ontcijferd_bericht = ""
    for letter in bericht:
        if letter in sleutel:
            ontcijferd_bericht += letter

    return ontcijferd_bericht
