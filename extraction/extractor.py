import re


def extract(messages):

    entities = set()
    claims = []

    for m in messages:

        text = m["text"]

        # -------------------------
        # Detect technologies
        # -------------------------

        if "Kafka" in text:
            entities.add(("Technology", "Kafka"))

        if "Spark" in text:
            entities.add(("Project", "Spark"))

        # -------------------------
        # Detect people (simple heuristic)
        # -------------------------

        sender = m["sender"]

        if sender:
            name = sender.split("@")[0]
            entities.add(("Person", name))

        # -------------------------
        # Detect decisions
        # -------------------------

        decision_keywords = [
            "decide",
            "decided",
            "should",
            "propose",
            "proposal",
            "suggest"
        ]

        for k in decision_keywords:

            if k in text.lower():

                decision = text[:120]

                entities.add(("Decision", decision))

                claims.append({
                    "subject": name,
                    "relation": "PROPOSED",
                    "object": decision,
                    "evidence": text,
                    "timestamp": m["timestamp"],
                    "source": m["id"]
                })

        # -------------------------
        # Technology usage
        # -------------------------

        if "Spark" in text and "Kafka" in text:

            claims.append({
                "subject": "Spark",
                "relation": "USES",
                "object": "Kafka",
                "evidence": text,
                "timestamp": m["timestamp"],
                "source": m["id"]
            })

    return list(entities), claims
