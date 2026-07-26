## Description: <br>
Use mdapi.io to convert documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mdapiio](https://clawhub.ai/user/mdapiio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agents use this skill to convert public webpages, uploaded documents, images, and text into compact Markdown, JSON, or prompt-transformed outputs through REST, MCP, ACP, A2A, and OpenAI-compatible interfaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User content is sent to the third-party mdapi.io service for conversion. <br>
Mitigation: Use only content approved for external processing; avoid secrets, credentials, regulated data, private source code, and internal URLs unless explicitly authorized. <br>
Risk: Paid-token and autonomous-payment flows can spend funds or expose reusable tokens if handled carelessly. <br>
Mitigation: Require clear user approval for payment, treat service payment responses as authoritative, and avoid storing paid tokens in shared or persistent tool configuration. <br>
Risk: Large inputs, inaccessible URLs, invalid tokens, rate limits, or payment failures can produce partial or failed conversions. <br>
Mitigation: Respect documented size and rate limits, handle HTTP 400/401/402/404/413/429/500 responses explicitly, and retry only when the service guidance supports it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mdapiio/skills/mdapi-conversion) <br>
- [mdapi.io service documentation](https://mdapi.io/) <br>
- [mdapi.io MCP endpoint](https://mdapi.io/mcp) <br>
- [mdapi.io health endpoint](https://mdapi.io/health) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or JSON responses with curl examples, API request shapes, protocol configuration snippets, and optional streaming SSE chunks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include converted markdown, prompt_result, resource metadata, token status, rate-limit headers, payment headers, or streaming progress markers.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence; artifact frontmatter states 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
