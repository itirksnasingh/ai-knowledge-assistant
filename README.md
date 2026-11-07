<div align="center">

# AI Knowledge Assistant

### Evidence-grounded document intelligence and question answering

**Python · Research-oriented AI · Reproducible experiments**

`IN PROGRESS` · Initial public project scaffold

</div>

---

## Overview

A research-oriented NLP system for comparing retrieval strategies and studying when generated answers are sufficiently supported by source evidence.

This repository is being developed as part of a portfolio exploring **reliable, explainable, and evidence-aware AI systems**. The current README describes the intended scope and methodology. Features are marked complete only after they have been implemented and tested.

## Problem statement

Retrieval-augmented generation can connect language-model outputs to external documents, but fluent answers are not necessarily correct or supported. Retrieval quality, source attribution, and the ability to abstain are therefore central design and evaluation concerns.

## Research question

> How do lexical, dense, and hybrid retrieval strategies compare on a defined document collection, and how should a question-answering system behave when retrieved evidence is insufficient?

## Objectives

- [ ] Document ingestion with page/section metadata
- [ ] BM25 lexical retrieval baseline
- [ ] Dense retrieval using sentence embeddings and FAISS
- [ ] Hybrid retrieval combining lexical and semantic signals
- [ ] Optional reranking experiment
- [ ] Evidence-linked answer generation with source references
- [ ] Abstention policy for insufficient or conflicting evidence

## Proposed methodology

The project will be developed through explicit baselines, documented implementation choices, and evaluation on a defined dataset or test collection. The exact experimental configuration and results will be added after implementation and validation.

## System architecture

The following diagram represents the **planned** system flow, not a claim that every component is already implemented.

```mermaid
flowchart TD\n A[PDF / text documents] --> B[Ingestion and parsing]\n B --> C[Chunks with source metadata]\n C --> D1[BM25 index]\n C --> D2[Embedding model + FAISS]\n D1 --> E[Retrieval comparison / hybrid fusion]\n D2 --> E\n E --> F[Evidence selection]\n F --> G{Evidence sufficient?}\n G -->|Yes| H[Grounded answer with citations]\n G -->|No| I[Abstain / request clarification]\n H --> J[Evaluation and feedback]
```

## Evaluation strategy

- Create a manually reviewed question–evidence set for the chosen document collection
- Measure Recall@K, Precision@K and MRR for retrieval
- Assess answer correctness and evidence support separately
- Test abstention on unanswerable or underspecified questions
- Report representative successes and failure cases

Evaluation results will be reported with dataset provenance, split strategy, relevant metrics, and representative failure cases. No performance figures are claimed in this initial scaffold.

## Technology stack

Python, Streamlit, Sentence Transformers, FAISS, BM25, PyMuPDF or pypdf, pandas, scikit-learn

## Repository structure

```text
ai-knowledge-assistant/
├── app.py                  # Streamlit entry point
├── src/
│   └── knowledge_assistant/
│       └── __init__.py
├── data/                   # Local datasets; large/private data excluded from Git
├── reports/                # Experiment protocols and evaluation reports
├── assets/
│   └── screenshots/        # Add genuine application screenshots here
├── tests/                  # Automated tests
├── requirements.txt
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Getting started

### Prerequisites

- Python 3.10 or newer (verify package-specific compatibility during setup)
- Git
- A virtual environment

### Clone

```bash
git clone https://github.com/itirksnasingh/ai-knowledge-assistant.git
cd ai-knowledge-assistant
```

### Create a virtual environment

**Windows PowerShell**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies and run

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

The current app is an informational scaffold. Core project workflows will be added as development progresses.

## Development roadmap

- [ ] Repository scaffold and project documentation
- [ ] Document ingestion and metadata preservation
- [ ] BM25 and dense retrieval baselines
- [ ] Hybrid retrieval and optional reranking
- [ ] Evidence-grounded response generation
- [ ] Evaluation dataset and metrics
- [ ] Failure analysis and reproducibility notes
- [ ] Deployment and demo documentation

## Limitations and responsible use

- Results will depend on document quality, chunking, embedding model, and query distribution.
- A similarity score is not, by itself, proof that evidence supports an answer.
- Multilingual performance must be measured rather than assumed.
- Any LLM-generated response must be checked against retrieved passages.

## Current status

| Area | Status |
|---|---|
| Project scope and research question | Defined |
| Repository scaffold and documentation | Prepared |
| Core implementation | In progress |
| Evaluation and results | Pending |
| Deployment | Pending |

## Reproducibility and data policy

- Record dataset name, source, version, and license.
- Do not commit private, sensitive, or unlicensed data.
- Keep credentials in local environment variables or hosting secrets.
- Record model versions, random seeds, preprocessing, and evaluation configuration.
- Distinguish measured results from hypotheses and planned work.

## Author

**Sanskriti Singh**  
B.Tech Computer Science (AI/ML)  
Bharati Vidyapeeth (Deemed to be University)

## License

This project is released under the MIT License. Dataset, pretrained-model, and third-party component licenses remain subject to their respective terms.
