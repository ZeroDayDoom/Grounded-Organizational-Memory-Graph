import mailbox

from extraction.extractor import extract
from dedup.deduplicator import deduplicate_claims
from graph.graph_builder import build_graph
from retrieval.retrieval import build_index, search


def load_mbox_messages():

    messages = []

    mbox = mailbox.mbox("data/dev_spark_apache_org.mbox")

    for i, msg in enumerate(mbox):

        try:
            text = msg.get_payload()

            if isinstance(text, list):
                text = text[0].get_payload()

            messages.append({
                "id": i,
                "sender": msg["from"],
                "timestamp": msg["date"],
                "text": str(text)
            })

        except:
            continue

    return messages


def run():

    print("Loading Apache mailing list dataset")

    messages = load_mbox_messages()

    print("Extracting knowledge")

    entities, claims = extract(messages)

    print("Deduplicating claims")

    claims = deduplicate_claims(claims)

    print("Building graph")

    build_graph(entities, claims)

    print("Building retrieval index")

    index, texts = build_index(claims)

    print("Testing retrieval")

    search(index, texts, "Kafka streaming decision")

    print("Pipeline finished")


if __name__ == "__main__":
    run()