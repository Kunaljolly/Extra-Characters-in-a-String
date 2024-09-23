class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            dp[i] = dp[i-1] + 1
            for word in dictionary:
                if i >= len(word) and s[i-len(word):i] == word:
                    dp[i] = min(dp[i], dp[i-len(word)])
        return dp[-1]
