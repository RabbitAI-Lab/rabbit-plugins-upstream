## Description: <br>
Give voice and phone agents BlueColumn-backed memory for calls, meetings, journal entries, customer conversations, coaching sessions, and sales interactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers building voice or phone agents use this skill to store and recall conversation memory through BlueColumn. It supports continuity for caller context, voice journaling, CRM notes, meeting summaries, coaching progress, sales objections, follow-ups, and customer history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Voice transcripts, caller details, customer records, journal entries, meetings, coaching notes, and sales history may be sent to BlueColumn for searchable storage and recall. <br>
Mitigation: Use explicit participant consent, redact sensitive content before storage, minimize what is sent, and define retention and deletion rules before production use. <br>
Risk: Stored memories may be recalled in the wrong context if caller or user identity is not scoped and verified. <br>
Mitigation: Gate recall by verified user or caller identity, use tenant-aware scoping, and avoid raw phone numbers as the sole memory identifier. <br>
Risk: External storage of personal or business conversation history may create privacy, confidentiality, or compliance obligations. <br>
Mitigation: Review organizational requirements before deployment and limit use to data categories approved for BlueColumn processing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/voice-memory-features) <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Code, API calls, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Python modules and Markdown usage examples with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLUECOLUMN_API_KEY; sends memory and recall requests to BlueColumn endpoints when used.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact/SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
