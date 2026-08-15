impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut counts = [0i32; 26];
        for (bs, bt) in s.bytes().zip(t.bytes()) {
            counts[(bs - b'a') as usize] += 1;
            counts[(bt - b'a') as usize] -= 1;
        }
        counts.iter().all(|&count| count == 0)
    }
}
