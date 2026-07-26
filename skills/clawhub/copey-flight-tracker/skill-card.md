## Description: <br>
Track flights in real time with detailed status, gate information, delays, and live position. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[copey02](https://clawhub.ai/user/copey02) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to look up real-time flight status by IATA flight number, then return formatted flight details or raw JSON for follow-up processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented free AviationStack setup sends the API key and flight lookup over plain HTTP. <br>
Mitigation: Use a dedicated low-value API key, rotate it if exposed, avoid sensitive lookups on untrusted networks, and prefer an HTTPS-capable plan or another provider for production or private use. <br>
Risk: Flight numbers and lookup activity are sent to AviationStack. <br>
Mitigation: Use the skill only when sharing the requested flight number with AviationStack is acceptable. <br>
Risk: The free AviationStack tier is limited to 100 requests per month. <br>
Mitigation: Track usage, handle rate-limit errors, or use a paid or alternative flight-data provider for heavier usage. <br>


## Reference(s): <br>
- [AviationStack API Setup](references/api-setup.md) <br>
- [AviationStack Free API Signup](https://aviationstack.com/signup/free) <br>
- [AviationStack Flights API Endpoint](http://api.aviationstack.com/v1/flights) <br>
- [ClawHub Skill Release](https://clawhub.ai/copey02/skills/copey-flight-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown-style terminal text or pretty-printed JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AVIATIONSTACK_API_KEY and outbound API access to AviationStack; the documented free tier uses HTTP.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
