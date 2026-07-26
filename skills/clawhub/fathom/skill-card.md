## Description: <br>
Connect to Fathom AI to fetch call recordings, transcripts, and summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucassynnott](https://clawhub.ai/user/lucassynnott) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and end users with authorized Fathom access use this skill to configure Fathom API credentials, list and search meetings, retrieve transcripts, fetch summaries and action items, and optionally register transcript webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Webhook setup can forward transcripts, summaries, and action items to a supplied HTTPS endpoint on an ongoing basis. <br>
Mitigation: Run webhook setup only for endpoints you control, and confirm retention, access controls, and deletion procedures before enabling delivery. <br>
Risk: The Fathom API key may expose meeting recordings, transcripts, summaries, and participant information. <br>
Mitigation: Use the skill only with authorized Fathom access, store the key with restrictive permissions or in an environment variable, and rotate it if it may have been exposed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/lucassynnott/skills/fathom) <br>
- [Fathom AI](https://fathom.video) <br>
- [Fathom Developer Portal](https://developers.fathom.ai) <br>
- [Fathom External API Base URL](https://api.fathom.ai/external/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Markdown, plain text, JSON, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq, and uses a Fathom API key from FATHOM_API_KEY or ~/.fathom_api_key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
