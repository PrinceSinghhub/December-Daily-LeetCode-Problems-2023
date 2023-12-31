class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        Min1 = min(prices)
        prices.remove(Min1)
        Min2 = min(prices)

        cost = money - (Min1 + Min2)
        if cost < 0:
            return money
        return cost
