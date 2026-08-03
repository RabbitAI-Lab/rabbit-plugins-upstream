## Description: <br>
Use mdapi.io to convert documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mdapiio](https://clawhub.ai/user/mdapiio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to convert public URLs, files, images, webpages, or raw text into Markdown, JSON, or prompt-shaped structured output for LLM workflows. It is also used to choose REST, MCP, ACP, A2A, or OpenAI-compatible access paths and to handle paid token activation when required. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Autonomous crypto payments can be irreversible and the security evidence notes no clear per-payment confirmation or spending cap. <br>
Mitigation: Require explicit user confirmation and a spending limit before wallet payment, avoid placing tokens or memos in URLs, and use local or trusted QR rendering for payment payloads. <br>
Risk: Selected content is sent to mdapi.io for conversion. <br>
Mitigation: Only send content the user is authorized to process, and avoid credentials, regulated data, proprietary material, or internal URLs unless the user has explicitly approved that use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mdapiio/skills/mdapi-conversion) <br>
- [mdapi.io service documentation](https://mdapi.io/) <br>
- [mdapi.io MCP endpoint](https://mdapi.io/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, API calls, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, REST or protocol-specific request guidance, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stream long conversions and may include token or payment status metadata.] <br>

## Skill Version(s): <br>
0.1.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
