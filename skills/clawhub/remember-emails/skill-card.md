## Description: <br>
Tracks email threads, promised actions, and follow-ups so agents can recall pending commitments and deadlines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents that manage email correspondence use this skill to store thread state, recall open promises or deadlines, and draft follow-ups with current context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email-thread summaries may include customer, legal, financial, personnel, or confidential business information sent to an external persistent memory API. <br>
Mitigation: Use a scoped and revocable API key, redact sensitive details where possible, and avoid sending full thread contents. <br>
Risk: Stored thread state may persist beyond the immediate email workflow. <br>
Mitigation: Confirm BlueColumn retention and deletion controls before using the skill with sensitive or regulated correspondence. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash code blocks and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY; requests use text, q, tags, and optional title fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
