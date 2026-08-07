impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut counts = [0i32; 26];

        for (b1, b2) in s.bytes().zip(t.bytes()) {
            counts[(b1 - b'a') as usize] += 1;
            counts[(b2 - b'a') as usize] -= 1;
        }
        counts.iter().all(|&count| count == 0)
    }
}
