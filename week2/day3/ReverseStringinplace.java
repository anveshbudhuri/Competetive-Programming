import java.util.Arrays;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static char[] reverse(char[] arrayOfChars) {

        // reverse input array of characters in place
        int i = 0,n = arrayOfChars.length;
        char temp;
    
        if(n==0)
            return arrayOfChars;
        n--; 
        while(i < n){
            temp = arrayOfChars[i];
            arrayOfChars[i] = arrayOfChars[n];
            arrayOfChars[n] = temp;
    
            i += 1;
            n -= 1;
            
        }
    
    
    
        return arrayOfChars;

    }


















    // tests

    @Test
    public void emptyStringTest() {
        final char[] expected = "".toCharArray();
        final char[] actual = "".toCharArray();
        reverse(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void singleCharacterStringTest() {
        final char[] expected = "A".toCharArray();
        final char[] actual = "A".toCharArray();
        reverse(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void longerStringTest() {
        final char[] expected = "EDCBA".toCharArray();
        final char[] actual = "ABCDE".toCharArray();
        reverse(actual);
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