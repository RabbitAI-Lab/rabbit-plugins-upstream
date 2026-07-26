## Description: <br>
Creates an AI meeting in LegionClaw for the current user session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
LegionClaw users and agents use this skill to create an AI meeting tied to the current session and return the meeting number to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting creation sends a session-derived identifier to the LegionClaw backend. <br>
Mitigation: Install only in LegionClaw environments where agents are allowed to create meetings, and avoid exposing full session identifiers or internal agent IDs in user-facing responses. <br>
Risk: Casual meeting requests may trigger real meeting creation. <br>
Mitigation: Use the skill for explicit meeting-creation intents and report success only after the backend business code indicates success. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/legionclaw-create-ai-meeting) <br>
- [LegionClaw meeting creation endpoint](https://legion.tongfudun.com/im/meeting/saveMeeting/v1ForAi) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown text with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a user-facing meeting creation message and meeting number when the backend reports business success.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
