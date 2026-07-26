## Description: <br>
Get Google's AI Mode answer for a query as structured JSON \u2014 AI-generated text blocks, cited references, and shopping results for commercial queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to retrieve Google's AI Mode answer for a question through Scavio, including answer text, cited references, and shopping results for commercial queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries and optional region or location parameters are sent to Scavio. <br>
Mitigation: Avoid secrets, private personal details, and sensitive business queries unless Scavio's data handling terms fit the use case. <br>
Risk: AI Mode answers and cited references can be incomplete, stale, or misleading. <br>
Mitigation: Return the API data without fabrication and surface references so users can verify sources before relying on the answer. <br>
Risk: Each request consumes one Scavio credit and may hit rate or usage limits. <br>
Mitigation: Confirm query intent before calling the API, track credit use, and handle 429 responses by waiting before retrying. <br>
Risk: The skill requires a Scavio API key. <br>
Mitigation: Read the key from SCAVIO_API_KEY and do not hardcode, log, or expose it in generated output. <br>


## Reference(s): <br>
- [Scavio Google AI Mode documentation](https://scavio.dev/docs/google-ai-mode) <br>
- [Scavio rate limits](https://scavio.dev/docs/rate-limits) <br>
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/scavio-google-ai-mode) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and inline shell or Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each API request costs 1 credit; ClawHub metadata declares a 90 second timeout and throttle of 1.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
