
def deduplicate_claims(claims):

    seen = set()
    unique = []

    for c in claims:
        key = (c["subject"], c["relation"], c["object"])

        if key not in seen:
            unique.append(c)
            seen.add(key)

    return unique

