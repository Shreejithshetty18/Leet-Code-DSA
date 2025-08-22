class Solution {
    public int maxProfit(int[] prices) {
        int max=0;
        int best=prices[0];
        for(int i=1;i<prices.length;i++){
            int p=prices[i]-best;
            max=Math.max(max,p);
            best=Math.min(best,prices[i]);

            

        }
        return max;
        
    }
}