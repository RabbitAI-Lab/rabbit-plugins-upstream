## Description: <br>
Veritier Fact Checking helps agents extract falsifiable claims from text or documents, verify them against live web evidence or private references, and run document authenticity scans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[salomonhenao](https://clawhub.ai/user/salomonhenao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, editors, and AI-agent operators use this skill to fact-check draft text, articles, AI-generated answers, URLs, and documents before relying on or publishing them. It can also support hallucination audits, disinformation screening, private-reference verification, and document authenticity checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fact-checking inputs, document contents, URLs, and private references are sent to Veritier's hosted API. <br>
Mitigation: Use the skill only when that processing is permitted, and avoid submitting secrets, personal data, regulated records, or internal documents unless approved by the organization. <br>
Risk: The Veritier API key authorizes access to the hosted service. <br>
Mitigation: Store the key in the required environment variable, send it only to the documented Veritier API endpoint, and rotate it if it is exposed. <br>
Risk: Example webhook receivers process externally delivered results. <br>
Mitigation: Verify the HMAC-SHA256 webhook signature against the raw request body before parsing or trusting the payload. <br>
Risk: The Flask webhook example is not suitable for public production deployment with debug mode enabled. <br>
Mitigation: Disable debug mode for public servers, deploy behind production infrastructure, and pin dependencies for production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/salomonhenao/skills/veritier-fact-checking) <br>
- [Veritier website](https://veritier.ai) <br>
- [Veritier documentation](https://veritier.ai/docs) <br>
- [Veritier API base](https://api.veritier.ai) <br>
- [Veritier MCP endpoint](https://api.veritier.ai/mcp/) <br>
- [Veritier dashboard](https://veritier.ai/dashboard) <br>
- [Published skill file](https://veritier.ai/skill.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON or text API responses, and Python or JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include extracted claims, verdicts, confidence scores, explanations, source URLs, MCP configuration, REST examples, and webhook setup guidance.] <br>

## Skill Version(s): <br>
3.0.1 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
