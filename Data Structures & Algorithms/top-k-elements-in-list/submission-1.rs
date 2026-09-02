impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let mut counts = HashMap::with_capacity(n);
        for num in nums {
            *counts.entry(num).or_insert(0) += 1;
        }
        let mut buckets: Vec<Vec<i32>> = vec![vec![]; n+1];
        for (num, freq) in counts {
            buckets[freq].push(num);
        }
        let mut results = Vec::with_capacity(k as usize);
        for bucket in buckets.into_iter().rev() {
            for num in bucket {
                results.push(num);
                if results.len() == k as usize {
                    return results;
                }
            }
        }
        results
    }
}
