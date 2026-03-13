# Recommendation Agent

class RecommendationAgent:

    def recommend(self, interest):
        data = {
            "AI": ["Machine Learning", "Deep Learning"],
            "Web": ["JavaScript", "React"]
        }
        return data.get(interest, [])

agent = RecommendationAgent()

print(agent.recommend("AI"))