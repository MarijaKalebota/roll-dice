package hello;

import org.springframework.web.bind.annotation.RestController;

import java.util.Random;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class HelloController {

    @RequestMapping("/")
    public String index() {
        StringBuilder greetingSB = new StringBuilder();
        greetingSB.append("Welcome to the dice rolling app!<br><br>");
        greetingSB.append("Options:<br>");
        greetingSB.append("\"/roll/<i>die_size</i>\" - Rolls a die of size <i>die_size</i>");

        return greetingSB.toString();
    }

    @RequestMapping("/roll/{die_size}")
    public String roll_size(@PathVariable Integer die_size) {
        try {
            Random rand = new Random();
            return ((Integer)(rand.nextInt(6)+1)).toString();
            
        } catch (Exception e) {
            //TODO: handle exception
            return "There was an error! Make sure you are inputting the size of the die as a number.";
        }
    }

}