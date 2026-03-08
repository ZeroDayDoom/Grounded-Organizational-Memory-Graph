
from neo4j import GraphDatabase
from config import URI, USERNAME, PASSWORD

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def build_graph(entities, claims):

    with driver.session() as session:

        for e in entities:
            session.run(
                "MERGE (n:Entity {name:$name,type:$type})",
                name=e[1],
                type=e[0]
            )

        for c in claims:
            session.run(
                '''
                MATCH (a:Entity {name:$sub})
                MATCH (b:Entity {name:$obj})

                MERGE (a)-[:CLAIM {
                    relation:$rel,
                    evidence:$ev,
                    timestamp:$ts,
                    source:$src
                }]->(b)
                ''',
                sub=c["subject"],
                obj=c["object"],
                rel=c["relation"],
                ev=c["evidence"],
                ts=c["timestamp"],
                src=c["source"]
            )
