## Description: <br>
Atomic Mail lets an AI agent read and write email through a programmable JMAP inbox with proof-of-work authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atomicmail](https://clawhub.ai/user/atomicmail) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use Atomic Mail to register or connect an inbox, list and triage messages, and send email, replies, or attachments through JMAP from an agent runtime. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive email contents and credential material. <br>
Mitigation: Install it only for intended Atomic Mail inbox access, keep the credential directory secret, and avoid syncing or committing generated credentials or JWT files. <br>
Risk: Agent-initiated sending, replying, forwarding, or attaching files can disclose information or send unintended messages. <br>
Mitigation: Require explicit human review before outbound email actions or attachment use. <br>
Risk: Hourly inbox polling can deliver inbox previews and summaries to the configured destination. <br>
Mitigation: Enable polling only when the destination is acceptable for receiving message summaries. <br>


## Reference(s): <br>
- [Atomic Mail ClawHub Listing](https://clawhub.ai/atomicmail/skills/atomicmail) <br>
- [Atomic Mail Homepage](https://atomicmail.ai) <br>
- [OpenClaw Cron Jobs](https://docs.openclaw.ai/automation/cron-jobs) <br>
- [Hermes Cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON/JMAP request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create credential files and JWT files in the configured Atomic Mail credentials directory; JMAP calls can return JSON email data.] <br>

## Skill Version(s): <br>
0.3.25 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
