## Description: <br>
Use mdapi.io to convert documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mdapiio](https://clawhub.ai/user/mdapiio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to convert public URLs, uploaded files, images, webpages, or raw text into Markdown or structured data for LLM workflows. It also guides use of mdapi.io payment, token activation, streaming, REST, MCP, ACP, A2A, and OpenAI-compatible access paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to make irreversible crypto payments or activate paid tokens without an explicit user confirmation step. <br>
Mitigation: Require user confirmation and spending limits before wallet-connected or autonomous payment; verify mdapi.io 402 payment details and token activation data before proceeding. <br>
Risk: Selected documents, URLs, text, and payment headers are sent to a third-party service. <br>
Mitigation: Do not submit credentials, regulated data, proprietary content, or payment tokens unless the user has authorized that data transfer; avoid logging tokens, memos, and signatures. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mdapiio/skills/mdapi-conversion) <br>
- [mdapi.io documentation](https://mdapi.io/) <br>
- [mdapi.io MCP endpoint](https://mdapi.io/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, JSON, and concise instructions with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include streaming conversion output, token or payment status guidance, and API request examples.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
