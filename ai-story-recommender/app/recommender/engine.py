from dataclasses import dataclass


@dataclass(frozen=True)
class Story:
    id: str
    title: str
    tags: tuple[str, ...]


STORIES = [
    Story("story-001", "The Last Train North", ("mystery", "adventure", "school")),
    Story("story-002", "Sherlock at Midnight", ("mystery", "detective", "adventure")),
    Story("story-003", "Stars Over Blackwater", ("romance", "fantasy", "school")),
    Story("story-004", "Escape from Raven Hall", ("thriller", "school", "adventure")),
    Story("story-005", "The Clockwork Heart", ("romance", "fantasy", "mystery")),
]


class RecommendationEngine:
    """Small, deterministic baseline suitable for later ML replacement."""

    def recommend(self, interests: list[str], limit: int = 3) -> list[dict]:
        normalized = {item.strip().lower() for item in interests if item.strip()}

        ranked = []
        for story in STORIES:
            matches = normalized.intersection(story.tags)
            score = len(matches)
            ranked.append(
                {
                    "id": story.id,
                    "title": story.title,
                    "score": score,
                    "matched_interests": sorted(matches),
                }
            )

        ranked.sort(key=lambda item: (-item["score"], item["title"]))
        return ranked[:limit]
