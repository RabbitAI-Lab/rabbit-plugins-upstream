## Description: <br>
Guides agents through cautious Meta Business Suite operations for authorized Instagram Business accounts, including DM and comment replies, quotas, stop conditions, local recaps, and human escalation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators, agencies, and developers use this skill to run careful inbound Instagram DM and comment workflows through Meta Business Suite on accounts they own or are authorized to operate. It helps an agent configure quotas, local memory files, reply rules, recap output, and escalation behavior so automation stops when the platform or a user requires human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent could be used on an Instagram account the operator is not authorized to run. <br>
Mitigation: Install and invoke the skill only for accounts the operator owns or is contractually authorized to operate, and only where automated replies are permitted for that account type. <br>
Risk: Run recaps can include handles and lead details if webhook alerts are enabled. <br>
Mitigation: Leave the webhook empty by default, keep recaps on disk, or redact recap details before enabling Telegram, Slack, Discord, or similar alert delivery. <br>
Risk: Platform challenges, action blocks, reauthentication screens, or account warnings can indicate that automation should stop. <br>
Mitigation: Stop the run, alert a human, and avoid solving challenges, retrying login, appealing suspensions, or changing timing to work around platform defenses. <br>
Risk: Excessive, duplicated, or poorly timed replies can look like spam and harm the account. <br>
Mitigation: Use the documented phase gates, per-run and daily quotas, seven-day dedupe checks, varied reply text, and manual review before moving from Phase A to Phase B. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexbloch-ia/skills/instagram-account-operations) <br>
- [Publisher profile](https://clawhub.ai/user/alexbloch-ia) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with YAML configuration examples, bash snippets, checklists, and recap templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local memory-file instructions and optional webhook recap guidance; it does not handle passwords or perform login flows.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
