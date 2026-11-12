## Description:

自动领取 WorkBuddy（原 CodeBuddy）每日签到积分，并可查询签到状态与签到周报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy users can use this skill to claim daily check-in points and review their check-in status, streak, and missed days. Run it only when the user explicitly identifies WorkBuddy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports key extraction, storage, and debugger activity beyond the stated daily check-in purpose; some files were only partly inspected.

Mitigation: Before installing, verify those capabilities are necessary and acceptable. Treat the scan as a warning about security concerns, not evidence of malicious intent.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/oracis/skills/workbuddy-checkin)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Brief check-in status text or a JSON status/report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include claim result, points, streak, and missed-day information.]

## Skill Version(s):

1.5.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
