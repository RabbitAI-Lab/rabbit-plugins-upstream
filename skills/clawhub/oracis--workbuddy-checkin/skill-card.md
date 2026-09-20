## Description:

Automatically claims daily WorkBuddy points, or checks the current check-in status, using the user's existing local WorkBuddy session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy users and automation-focused agents use this skill to claim daily check-in points without opening the client UI, or to report status-only details such as streak days, total points, and today's claim result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads the local WorkBuddy or CodeBuddy session token and uses it for authenticated WorkBuddy requests.

Mitigation: Review the skill before installing, use explicit WorkBuddy-specific commands, and keep status checks in status-only mode when no claim should be made.

Risk: Broad check-in triggers could claim points when the user only intended to ask about current status.

Mitigation: Prefer status-only execution for questions, and enable scheduled runs only when automatic daily claims are intentional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oracis/skills/workbuddy-checkin)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with command-line status text and optional JSON from the bundled script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local WorkBuddy credentials, supports status-only mode, and returns concise success, skip, info, or failure messages.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
