class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)

        benefits = []

        for i, (factor, price) in enumerate(items):
            free = 0

            for j, (other_factor, other_price) in enumerate(items):
                if i != j and other_factor % factor == 0:
                    free += 1

            benefits.append(free)

        dp = [0] * (budget + 1)

        for i, (factor, price) in enumerate(items):

            old = dp[:]
            new = old[:]

            first_value = 1 + benefits[i]

            for b in range(price, budget + 1):

                first_purchase = old[b - price] + first_value

                extra_purchase = new[b - price] + 1

                new[b] = max(
                    old[b],
                    first_purchase,
                    extra_purchase
                )

            dp = new

        return dp[budget]
