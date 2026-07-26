## Description: <br>
Make international phone calls to any country with low per-minute rates and payment through PayPal or UPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adisahani](https://clawhub.ai/user/adisahani) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to set up Ringez access, check calling balance, initiate international phone calls in bridge or direct mode, manage active calls, send DTMF tones, and review call history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid external phone calls can create charges or contact unintended recipients. <br>
Mitigation: Require explicit approval for each destination number, direct versus bridge mode, expected cost, and maximum duration before initiating a call. <br>
Risk: Calls, DTMF entry, transcripts, and webhook forwarding may expose sensitive communications or regulated data. <br>
Mitigation: Use only with verified consent and legal compliance; avoid batch campaigns, sales outreach, transcript analytics, and webhook forwarding unless spending limits, retention, and data controls are confirmed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/adisahani/skills/phone-calling) <br>
- [Ringez API base](https://ringez-api.vercel.app/api/v1) <br>
- [Ringez quickstart guide](artifact/ringez-quickstart-guide.md) <br>
- [Ringez API specification](artifact/ringez-api-spec.md) <br>
- [Ringez implementation guide](artifact/ringez-implementation-guide.md) <br>
- [OpenAPI specification](artifact/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, configuration] <br>
**Output Format:** [Markdown with HTTP request examples and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Ringez session or account and user approval before paid call actions.] <br>

## Skill Version(s): <br>
1.0.7 (source: SKILL.md frontmatter, CHANGELOG, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
