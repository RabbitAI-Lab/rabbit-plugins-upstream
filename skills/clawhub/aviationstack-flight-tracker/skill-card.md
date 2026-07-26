## Description: <br>
Track commercial flights with AviationStack and return status, gate, delay, aircraft, and live position details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[copey02](https://clawhub.ai/user/copey02) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to look up a flight by IATA flight number and present current flight status, departure and arrival details, delays, and live position information to end users. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The default AviationStack free-tier setup sends the API key and flight lookup over unencrypted HTTP. <br>
Mitigation: Use a limited-purpose key, avoid public or untrusted networks, do not store the key permanently on shared or synced machines, and prefer an HTTPS-capable paid plan or another provider for sensitive travel use. <br>


## Reference(s): <br>
- [AviationStack API Setup](references/api-setup.md) <br>
- [AviationStack Free API Signup](https://aviationstack.com/signup/free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Formatted console text with Markdown-style emphasis, or raw JSON when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an AVIATIONSTACK_API_KEY environment variable and network access to AviationStack; the documented free tier is limited to 100 requests per month.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
