## Description: <br>
Use mdapi.io to convert documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mdapiio](https://clawhub.ai/user/mdapiio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route documents, images, webpages, or raw text through mdapi.io and receive compact Markdown or structured results for downstream LLM workflows. It also guides protocol selection for REST, MCP, ACP, A2A, and OpenAI-compatible access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected documents, text, prompts, and URLs to the third-party mdapi.io service. <br>
Mitigation: Do not use it with secrets, private or internal URLs, regulated data, or proprietary files unless the use has been explicitly approved. <br>
Risk: The skill can guide agents through cryptocurrency payment and token activation flows. <br>
Mitigation: Independently verify the amount, token, network, wallet address, memo, and service identity before payment, and use connected-wallet autonomous payments only with strict spending controls. <br>
Risk: The security scan verdict is suspicious because payment and data-transfer behaviors require user trust. <br>
Mitigation: Review the skill, scanner summary, and service terms before installation or deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mdapiio/skills/mdapi-conversion) <br>
- [mdapi.io service](https://mdapi.io/) <br>
- [mdapi.io MCP endpoint](https://mdapi.io/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include converted Markdown, prompt results, token status, metadata, streaming chunks, or protocol configuration snippets.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
