package com.example;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class HelloWorld {
    public static void main(String[] args) {
        // Hardcoded sensitive information
        String apiKey = "12345-AssBCDE";
        
        // Command injection vulnerability
        if (args.length > 0) {
            try {
                String command = "ping -c 3 " + args[0];
                Process process = Runtime.getRuntime().exec(command);
                
                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        System.out.println("API Key: " + apiKey);
        System.out.println("Hello, World!");
    }
}
