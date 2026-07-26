## Description: <br>
Intelligent LLM proxy that routes requests to appropriate models based on complexity. Save money by using cheaper models for simple tasks. Tested with Anthropic, OpenAI, Gemini, Kimi/Moonshot, and Ollama. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexrudloff](https://clawhub.ai/user/alexrudloff) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to set up and operate an LLM routing proxy that classifies request complexity and sends requests to configured local or remote model providers to manage cost and model selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provider API keys or OAuth tokens may be exposed through local configuration files or shell history. <br>
Mitigation: Protect credentials in config files, avoid sharing them in prompts or logs, and rotate keys if exposure is suspected. <br>
Risk: Prompts routed to remote providers may contain sensitive information subject to those providers policies. <br>
Mitigation: Review provider policies before sending sensitive prompts and use local routing options when remote disclosure is not acceptable. <br>
Risk: Automatic model routing can create unexpected provider billing or background service use. <br>
Mitigation: Monitor provider billing and enable the LaunchAgent only when continuous background routing is intended. <br>
Risk: Binding the proxy beyond localhost can expose the routing API to unintended clients. <br>
Mitigation: Keep the server bound to localhost unless external access is intentional and separately secured. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexrudloff/skills/llmrouter) <br>
- [Llmrouter homepage](https://github.com/alexrudloff/llmrouter) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash, JSON, YAML, and XML snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes setup, provider configuration, testing, service, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
