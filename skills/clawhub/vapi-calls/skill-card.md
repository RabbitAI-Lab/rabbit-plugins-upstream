## Description: <br>
Advanced AI voice assistant for phone calls capable of persuasion, sales, restaurant bookings, reminders, and notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmorillas99-cyber](https://clawhub.ai/user/cmorillas99-cyber) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External teams and developers use this skill to initiate Vapi-powered autonomous phone calls for defined missions and receive structured call results. It is suited for workflows that deliberately require phone outreach, reminders, notifications, bookings, or sales-style voice interaction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place real autonomous phone calls through the user's Vapi account. <br>
Mitigation: Confirm the recipient, purpose, cost, consent, and legal basis before each call, including applicable AI disclosure, telemarketing, and recording or transcription requirements. <br>
Risk: The skill requires an internet-reachable webhook for real-time call updates. <br>
Mitigation: Expose the webhook only through a controlled tunnel, keep the endpoint active only while needed, and avoid publishing unrestricted local services. <br>
Risk: Call transcripts, summaries, costs, and identifiers may be stored in local logs. <br>
Mitigation: Protect access to the local workspace and regularly review or delete call logs that contain sensitive call records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cmorillas99-cyber/skills/vapi-calls) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [JSON call result plus Markdown configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The call result can include status, call ID, transcript, summary, cost, ended reason, duration, and a local log file path when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
