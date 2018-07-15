import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class FindDuplicates {
    private static MessageDigest messageDigest;
    static {
        try {
            messageDigest = MessageDigest.getInstance("SHA-512");
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("error", e);
        }
    }

    public static void findDuplicateFiles(Map<String, List<String>> filesList, File directory) {
        for (File dirChild : directory.listFiles()) {
            // sub directories recursively
            if (dirChild.isDirectory()) {
                findDuplicateFiles(filesList, dirChild);
            } else {
                try {
                	// Read file
                    FileInputStream fileInput = new FileInputStream(dirChild);
                    byte fileData[] = new byte[(int) dirChild.length()];
                    fileInput.read(fileData);
                    fileInput.close();
                    // Create hash
                    String uniqueFileHash = new BigInteger(1, messageDigest.digest(fileData)).toString(16);
                    List<String> identicalList = filesList.get(uniqueFileHash);
                    if (identicalList == null) {
                        identicalList = new LinkedList<String>();
                    }
                    // Add to list
                    identicalList.add(dirChild.getAbsolutePath());
                    // push updated list to Hash table
                    filesList.put(uniqueFileHash, identicalList);
                } catch (IOException e) {
                    throw new RuntimeException("error" + dirChild.getAbsolutePath(), e);
                }
            }
        }
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("No directory path given");
            return;
        }
        File dir = new File(args[0]);
        if (!dir.isDirectory()) {
            System.out.println("Directory does not exist");
            return;
        }
        Map<String, List<String>> lists = new HashMap<String, List<String>>();
        FindDuplicates.findDuplicateFiles(lists, dir);
        for (List<String> list : lists.values()) {
            if (list.size() > 1) {
                System.out.println("\n");
                for (String file : list) {
                    System.out.println(file);
                }
            }
        }
        System.out.println("\n");
    }

}