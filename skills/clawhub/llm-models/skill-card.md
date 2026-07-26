## Description: <br>
Llm Models helps agents access Claude, Gemini, Kimi, GLM and other language models through the inference.sh CLI using OpenRouter. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, engineers, and agents use this skill to find and run hosted LLMs for coding, writing, analysis, chat, and agent workflows through OpenRouter-backed inference.sh commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an external installer and CLI distribution path. <br>
Mitigation: Review the installer source before use and prefer the manual or checksummed installation path when available. <br>
Risk: Prompts, system messages, files, and generated task context may be shared with inference.sh, OpenRouter, and downstream model providers. <br>
Mitigation: Do not send secrets, private credentials, regulated data, or proprietary code unless that use is approved. <br>
Risk: Automatic model fallback and cost optimization can change which hosted model processes a request. <br>
Mitigation: Choose explicit model app IDs for workloads that require predictable provider behavior, cost, latency, or model characteristics. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okaris/skills/llm-models) <br>
- [inference.sh](https://inference.sh) <br>
- [inference.sh CLI installer](https://cli.inference.sh) <br>
- [inference.sh CLI checksums](https://dist.inference.sh/cli/checksums.txt) <br>
- [Agents Overview](https://inference.sh/docs/concepts/agents) <br>
- [Agent SDK](https://inference.sh/docs/api/agent/overview) <br>
- [Building a Research Agent](https://inference.sh/blog/guides/research-agent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON input examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use the infsh CLI when the agent has Bash(infsh *) tool access.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
