## Description:

Uses an access token explicitly supplied by the user to check and claim daily WorkBuddy credits, and reports the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy users can use this skill to check daily check-in status and claim credits when they explicitly request a WorkBuddy check-in. If the user says only “check in” or “claim credits” without naming a service, the skill asks which service they mean.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks this release suspicious because marker or log writes may reach paths outside the skill directory; evidence for some referenced paths is incomplete.

Mitigation: Review marker and log path handling and the missing path references, then confirm the host runtime limits writes to intended locations before running.

## Reference(s):

- [WorkBuddy check-in skill page](https://clawhub.ai/oracis/skills/workbuddy-checkin)
- [WorkBuddy service](https://www.workbuddy.cn)
- [Tencent Copilot service](https://copilot.tencent.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Human-readable check-in status or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports check-in status, streak, and credit totals; supports status-only queries.]

## Skill Version(s):

1.5.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
