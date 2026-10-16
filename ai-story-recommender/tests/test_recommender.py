from app.recommender.engine import RecommendationEngine


def test_matching_interest_is_ranked_first():
    result = RecommendationEngine().recommend(["detective"])
    assert result[0]["id"] == "story-002"
    assert result[0]["score"] == 1


def test_empty_interests_returns_stable_results():
    result = RecommendationEngine().recommend([])
    assert len(result) == 3
    assert result[0]["score"] == 0
