## Description: <br>
Routes simple and medium-complexity model requests to local Ollama models to reduce cloud API cost, with DeepSeek cloud fallback for complex, tool-using, or large-context work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haydaymalzemeleri-ui](https://clawhub.ai/user/haydaymalzemeleri-ui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route agent responses between local Ollama models and DeepSeek cloud based on task complexity, tool needs, context size, and cost sensitivity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts may be handled by DeepSeek cloud when fallback is used. <br>
Mitigation: Use a local-only policy or require explicit confirmation before cloud fallback for private, regulated, or sensitive data. <br>
Risk: Local models may be unsuitable for tool use, large-context requests, multilingual needs, or current-information tasks. <br>
Mitigation: Route those requests to the cloud path as documented and review outputs before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haydaymalzemeleri-ui/skills/local-model-router) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with routing tables and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable code; documents local Ollama routing, cloud fallback, and model-selection limitations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
