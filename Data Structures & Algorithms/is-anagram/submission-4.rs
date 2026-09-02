impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut counts = [0i32; 26];
        for (s_b, t_b) in s.bytes().zip(t.bytes()) {
            counts[(s_b - b'a') as usize] += 1;
            counts[(t_b - b'a') as usize] -= 1;
        }        
        counts.iter().all(|&count| count == 0) 
    }
}
