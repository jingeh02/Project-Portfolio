# AI Story Recommender — Portfolio Project

> A practical AI application demonstrating recommendation architecture, personalization, API design, and production-minded engineering.

## Why I built it

Modern AI products are not only about calling a language model. A useful product must combine user behavior, content understanding, ranking, APIs, persistence, and reliable software architecture.

This project is designed as a focused demonstration of that engineering mindset.

## Concept

The system recommends story/content candidates based on:

- User preferences
- Recent interactions
- Content metadata
- Semantic similarity
- Simple ranking signals

It is intentionally designed so the recommendation engine can evolve from deterministic scoring to a learned model without requiring the application architecture to be rewritten.

## Architecture

```text
                    ┌──────────────────┐
                    │   Web / Mobile   │
                    │      Client      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     REST API     │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
       ┌────────────┐ ┌────────────┐ ┌────────────┐
       │ User       │ │ Content    │ │ Recommend  │
       │ Profile    │ │ Metadata   │ │ Engine     │
       └────────────┘ └────────────┘ └─────┬──────┘
                                           │
                              ┌────────────┴────────────┐
                              ▼                         ▼
                       ┌──────────────┐          ┌──────────────┐
                       │ Similarity   │          │ Ranking      │
                       │ / Embeddings │          │ / Scoring    │
                       └──────────────┘          └──────────────┘
```

## Engineering goals

### 1. Separate product logic from model logic

The recommendation API should not depend directly on one ML implementation.

```text
Application
    ↓
Recommendation Interface
    ↓
Ranking Strategy
    ├── Rule-based ranking
    ├── Similarity ranking
    └── ML ranking (future)
```

This makes experimentation easier and reduces coupling.

### 2. Build for measurable iteration

A recommendation system should be evaluated using observable signals rather than intuition alone.

Potential metrics include:

- Click-through rate
- Completion rate
- Session engagement
- Recommendation acceptance
- Diversity of recommendations

### 3. Handle the cold-start problem

For new users, the system can fall back to:

- Popular content
- Content categories
- Explicit preferences
- Semantic similarity from the first interaction

For new content, metadata and semantic representation can provide an initial ranking signal.

## Example scoring model

A simple first-stage ranker can combine several signals:

```text
score =
    w1 * preference_match
  + w2 * semantic_similarity
  + w3 * popularity
  + w4 * freshness
  - w5 * repetition_penalty
```

The weights are configuration rather than hard-coded business logic, allowing later experimentation.

## Why this project is relevant to AI products

The important engineering problem is not simply:

> "How do I call an AI model?"

It is:

> "How do I build a reliable software system around AI that can evolve as data, models, users, and product requirements change?"

That is the problem this project is intended to demonstrate.

## Planned implementation

- Python
- FastAPI
- Pydantic
- PostgreSQL
- Embedding-based similarity
- Configurable ranking pipeline
- Unit tests
- Docker
- API documentation

## Roadmap

- [ ] Basic content model
- [ ] User preference model
- [ ] REST API
- [ ] Deterministic recommendation engine
- [ ] Embedding similarity
- [ ] Ranking evaluation
- [ ] Dockerized deployment
- [ ] Automated tests
- [ ] Lightweight web client
- [ ] Experiment tracking

## Portfolio context

This project complements my professional experience in:

- AI-integrated applications
- Computer vision
- C/C++
- Qt
- Mobile development
- Real-time systems
- Enterprise software
- System architecture
- Technical project leadership

It is a deliberately focused modern project that demonstrates how I approach **AI + software architecture**, while my professional portfolio documents larger production projects whose source code is proprietary.

## Author

**Jinge H.**

**Senior Software Engineer | AI & Software Solutions Architect | Technical Project Lead**
