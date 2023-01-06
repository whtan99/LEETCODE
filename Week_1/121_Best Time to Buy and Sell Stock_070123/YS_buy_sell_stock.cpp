#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int curr_lowest = prices[0];
        int max_profit = 0;

        for (int i = 1; i < prices.size(); i++) {
            max_profit = max(max_profit, prices[i]-curr_lowest);
            curr_lowest = min(curr_lowest, prices[i]);
        }
        
        return max_profit;
    }
};