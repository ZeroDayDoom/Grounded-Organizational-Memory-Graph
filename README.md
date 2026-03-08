# Grounded Organizational Memory Graph

Author: Ankit Rewar  
Roll No: 23B2176  
IIT Bombay

## Overview

Organizations generate large volumes of knowledge through emails,
issue trackers and internal communication.
This project builds a system that converts unstructured communication
into a structured organizational memory graph.
The system extracts entities and claims from Apache Spark developer
mailing list discussions and stores them in a Neo4j knowledge graph.

Key capabilities:

• Structured entity and claim extraction  
• Evidence grounding  
• Deduplication and canonicalization  
• Graph-based knowledge storage  
• Semantic retrieval  
• Interactive graph visualization  

---

## Dataset

Apache Spark Developer Mailing List

https://mail-archives.apache.org/mod_mbox/spark-dev/

Each email contains

• sender  
• timestamp  
• thread metadata  
• message content

---

## System Architecture

Pipeline:


```markdown
Mailing List Archive
        │
        ▼
Structured Extraction
        │
        ▼
Deduplication
        │
        ▼
Neo4j Memory Graph
        │
        ▼
Semantic Retrieval
        │
        ▼
Visualization
```

## Ontology

### Entity Types

Person  
Project  
Technology  
Decision  
Issue  

### Relationship Types

PROPOSED  
USES  
AFFECTS  
DISCUSSES  

Example claim:

Spark → USES → Kafka

---

## Installation

Install dependencies

---

## Running the Pipeline

Step 1 — parse emails

Step 2 — extract entities and claims

Step 3 — deduplicate entities

Step 4 — build graph

Step 5 — run retrieval

Step 6 — visualization

---

## Example Query

Example retrieved context pack:

Claim:
Spark USES Kafka

Evidence:
"We should migrate Spark streaming to Kafka."

Timestamp:
2024-01-01

---

## Graph Query Example

Neo4j query:

---

## Visualization

The system provides an interactive graph explorer using

• Neo4j Browser  
• Streamlit

Users can explore entities and inspect evidence grounding.

---

## Contributions

This project demonstrates how organizational communication
can be transformed into a structured knowledge graph that
preserves institutional knowledge.

