## Description: <br>
Guides agents through FlashRev-powered email outreach with the flashrev-mailer CLI, including campaign planning, drafting, committing, monitoring, follow-up, reply triage, and optional AI auto-reply with explicit approval gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to have an agent prepare, inspect, and manage FlashRev outbound email campaigns through a CLI workflow. It is intended for campaign drafting, send approval, follow-up sequencing, mailbox-pool use, reply triage, and optional AI auto-reply setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward actions that affect real outbound email campaigns. <br>
Mitigation: Require explicit confirmation for every live send, reply, reschedule, delete, pause/resume, and AI auto-reply state change. <br>
Risk: Implicit activation could involve the agent in email outreach before the user intends it. <br>
Mitigation: Disable or constrain implicit activation where the host agent supports that control. <br>
Risk: Campaign, profile, and mailbox metadata may remain in local `.flashrev/` caches. <br>
Mitigation: Treat `.flashrev/` as sensitive local data and avoid committing, sharing, or leaving it on shared machines. <br>
Risk: Unspecified timezone settings can change when campaign messages are sent. <br>
Mitigation: Set the campaign timezone explicitly before live sending. <br>


## Reference(s): <br>
- [FlashRev API Contract (v2)](artifact/references/api_contract.md) <br>
- [Flashrev Mailer on ClawHub](https://clawhub.ai/legionspace-hackathon/skills/flashrev-mailer) <br>
- [FlashRev API Base URL](https://open-ai-api.flashlabs.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-oriented CLI output expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation for live send, direct reply, reschedule, delete, pause/resume, and AI auto-reply state changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
