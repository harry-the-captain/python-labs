class Solution {
    public boolean isValid(String s) {

        // without using stack
        // i used built methods of java to pop and push
        while (true) {
            if (s.contains("()")) {
                s = s.replace("()", "");
            } 
            else if (s.contains("{}")) {
                s = s.replace("{}", "");
            } 
            else if (s.contains("[]")) {
                s = s.replace("[]", "");
            } 
            else {
                // If the string becomes empty, it indicates all brackets are matched.
                return s.isEmpty();
            }
        }
    }
}
