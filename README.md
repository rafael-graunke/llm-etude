# LLM Etude
<p align="center">
  <img src="assets/brain.svg" width="200" alt="Icon of a brain">
</p>
<p align="center">
Tracking my studies through naive-first iteration of LLM concepts.
</p>

## Summary
In order to level up my SWE skills I decided to start learning more about LLM concepts like RAG, embedding, evals and etc. My goal at this moment is NOT to deep dive into all the ML nooks and crannies, I just want to get a grasp of app level integration with LLMs more in depth.

## Method
In this learning process I'll be using Claude to guide me through learning, which means helping me with concepts whenever I get stuck, help me with setting up my machine and most importantly building me study plan with references from reputable sources, which I'll be linking in the [Resources section](##resources).

**The most important thing is I will NOT use LLM prompts to write the code, any supporting docstring, comments or documentation.** This might be obvious, but is more of a shame note for myself if I fail to follow it.

Last but not least, the goal is to implement the bare minimum necessary to see the LLM concepts in action. The idea is to keep dependencies at a bare minimum without using specialized frameworks and etc, but at the same time not having to reimplement things from scratch, so [the list](#dependencies) may grow.

## Dependencies
Like mentioned above, I'm trying to keep the dependency list at a bare minimum. This is it's current state:

- **ipykernel:** required to run `.ipynb` files
- **litellm:** enables to make model calls more generically, so anyone can just change the `MODEL` constants and run the notebook. Also allows me to easily swap between models when going from my main desktop PC to my laptop, or just try out different models.

## Resources

- [**Claude Academy - Building with the Claude API**](https://academy.claude.com/courses/building-with-the-claude-api)

## Tools
This quickly covers the tools being used and the decision making behind those choises. Please adapt as you which to better fit your needs.

### Ollama
Since the goal is learning, I opted to have a local model running on my machine to not worry about spending anything while iterating over the code.

### Qwen 3
The model I picked was `qwen3:14b`, as suggested by Claude given my specs (RTX 5060TI 16GB VRAM). The model will probably be a constant on the code so can change on demand.


## Learning Path

1. [**LLM Prompting**](src/llm-prompting.ipynb) - Covers generally how to interact with LLM APIs.

2. [**Prompt Evaluation**](src/prompt-evaluation.ipynb) - Techniques for evaluating a prompt and improving it iteratively.

3. [**Prompt Engineering**](src/prompt-engineering.ipynb) - Techniques for improving prompt writing.

4. [**Tool Use**](src/tool-use.ipynb) - Understanding how models call tools.
