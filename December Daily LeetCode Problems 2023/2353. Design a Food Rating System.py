from sortedcontainers import SortedList, SortedKeyList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisineDict = collections.defaultdict(lambda:SortedKeyList(key=lambda x: (-x["rating"], x["food"])))
        self.foodDict = collections.defaultdict(str)
        for index, cuisine in enumerate(cuisines):
            food = foods[index]
            rating = ratings[index]
            self.cuisineDict[cuisine].add({ "food": food, "rating": rating })
            self.foodDict[food] = { "cuisine": cuisine, "oldRating": rating }

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodDict[food]["cuisine"]
        oldRating = self.foodDict[food]["oldRating"]
        self.cuisineDict[cuisine].discard({ "food": food, "rating": oldRating })
        self.cuisineDict[cuisine].add({ "food": food, "rating": newRating })
        self.foodDict[food]["oldRating"] = newRating
    def highestRated(self, cuisine: str) -> str:
        return self.cuisineDict[cuisine][0]["food"]