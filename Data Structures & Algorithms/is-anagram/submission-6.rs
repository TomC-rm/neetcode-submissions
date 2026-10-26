impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false
        }

        let mut count = [0i32; 26];
        for (sb, tb) in s.bytes().zip(t.bytes()) {
            count[(sb - b'a') as usize] += 1;
            count[(tb - b'a') as usize] -= 1;
        }
        return count.iter().all(|&count| count == 0)

    }
}
