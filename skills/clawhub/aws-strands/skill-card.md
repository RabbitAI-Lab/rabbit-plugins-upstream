## Description: <br>
Build and run Python-based AI agents using the AWS Strands SDK for autonomous agents, multi-agent workflows, custom tools, MCP integration, and model providers including Ollama, Anthropic, OpenAI, and Bedrock. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[trippingkelsea](https://clawhub.ai/user/trippingkelsea) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold and run Python Strands agents, configure model providers, add tools, connect MCP services, and build multi-agent patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated agents can read and write files and run shell commands without strong guardrails. <br>
Mitigation: Use an isolated Python environment or disposable workspace, review or remove default file and shell tools before running agents, and avoid repositories or directories containing secrets. <br>
Risk: Model providers, Bedrock defaults, MCP services, and A2A services may require cloud or API credentials. <br>
Mitigation: Use least-privilege credentials, avoid production credentials for testing, and connect only trusted MCP or A2A services. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/trippingkelsea/skills/aws-strands) <br>
- [Strands SDK](https://github.com/strands-agents/sdk-python) <br>
- [Strands SDK Cheatsheet](references/cheatsheet.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Files, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with Python and shell code blocks; helper scripts generate Python and Markdown files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated agents may include file read, file write, and shell command tools.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter states 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
