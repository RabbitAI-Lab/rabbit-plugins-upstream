## Description: <br>
Build and run Python-based AI agents using the AWS Strands SDK. Use when you need to create autonomous agents, multi-agent workflows, custom tools, or integrate with MCP servers. Supports Ollama (local), Anthropic, OpenAI, Bedrock, and other model providers. Use for agent scaffolding, tool creation, and running agent tasks programmatically. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[trippingkelsea](https://clawhub.ai/user/trippingkelsea) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold, configure, and run Python agents with Strands SDK providers, tools, MCP integrations, and multi-agent patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated agents can read and write local files and run shell commands. <br>
Mitigation: Review generated code before running it, remove or constrain shell and file-write tools, and use a sandbox or dedicated project directory. <br>
Risk: Agents may use API keys, cloud credentials, or MCP servers during execution. <br>
Mitigation: Use least-privilege credentials and load only trusted agent files and MCP servers. <br>


## Reference(s): <br>
- [Strands SDK](https://github.com/strands-agents/sdk-python) <br>
- [Strands SDK Cheatsheet](references/cheatsheet.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/trippingkelsea/skills/strands) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with Python and bash snippets; bundled scripts can generate Python agent project files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated agents may include local file read/write tools and shell command execution.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release metadata; artifact frontmatter says 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
