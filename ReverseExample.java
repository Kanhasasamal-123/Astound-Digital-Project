public class ReverseExample {
    public static void main(String[] args) {
        String input = "Hello World";
        
        // Method 1: Using StringBuilder
        String reversed = new StringBuilder(input).reverse().toString();
        System.out.println("Reversed (StringBuilder): " + reversed);

        // Method 2: Manual loop
        String manualReverse = "";
        for (int i = input.length() - 1; i >= 0; i--) {
            manualReverse += input.charAt(i);
        }
        System.out.println("Reversed (Manual Loop): " + manualReverse);
    }
}
