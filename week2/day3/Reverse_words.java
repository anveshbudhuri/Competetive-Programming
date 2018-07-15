import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.util.*;
import java.lang.*;
import static org.junit.Assert.*;

public class Solution {

    public static char[] reverseWords(char[] message) {

        // decode the message by reversing the words
        int length_of_msg = message.length;
        if(length_of_msg == 0)
            return message;

        reverse(message, 0, length_of_msg);

        int temp = 0;
        for(int k=0;k<length_of_msg;k++){
            if(message[k]==' '){
                reverse(message, temp, k);
                temp = k + 1;}
        }
        reverse(message, temp, length_of_msg);

        return message;

        

    }
    
    public static char[] reverse(char[] list_of_chars,int initial,int ending)
    {
    // # Reverse the input list of chars in place
        int i = initial;
        int j = ending;
        char temp;
    
        if(j == 0)
            return list_of_chars;
        j -= 1;
        while(i < j){
            temp = list_of_chars[i];
            list_of_chars[i] = list_of_chars[j];
            list_of_chars[j] = temp;
    
            i += 1;
            j -= 1;}
    
        return list_of_chars;
    }


















    // tests

    @Test
    public void oneWordTest() {
        final char[] expected = "vault".toCharArray();
        final char[] actual = "vault".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void twoWordsTest() {
        final char[] expected = "cake thief".toCharArray();
        final char[] actual = "thief cake".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void threeWordsTest() {
        final char[] expected = "get another one".toCharArray();
        final char[] actual = "one another get".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void multipleWordsSameLengthTest() {
        final char[] expected = "the cat ate the rat".toCharArray();
        final char[] actual = "rat the ate cat the".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void multipleWordsDifferentLengthsTest() {
        final char[] expected = "chocolate bundt cake is yummy".toCharArray();
        final char[] actual = "yummy is cake bundt chocolate".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void emptyStringTest() {
        final char[] expected = "".toCharArray();
        final char[] actual = "".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}