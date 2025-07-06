package org.example.mcpclient.controllers;

import org.example.mcpclient.agents.AIAgent;
import org.example.mcpclient.dtos.ChatRequest;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;


@CrossOrigin(origins = "http://localhost:4200")
@RestController
public class AIRestController {

    private AIAgent agent;
    public AIRestController(AIAgent agent) {
        this.agent = agent;
    }

    @PostMapping("/chat/send")
    public String chat(@RequestBody ChatRequest req){
        return agent.askLLM(req.query);
    }
}
