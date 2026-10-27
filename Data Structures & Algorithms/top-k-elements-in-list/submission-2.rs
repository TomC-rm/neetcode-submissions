impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let mut counts = HashMap::with_capacity(n); //counter for each num
        for n in nums {
            *counts.entry(n).or_insert(0) += 1;
        }

        let mut buckets = vec![vec![]; n + 1]; //create buckets of frequencies
        for (num, count) in counts {
            buckets[count].push(num);
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
