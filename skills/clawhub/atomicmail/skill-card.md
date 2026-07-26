## Description: <br>
Atomic Mail lets an AI agent read and write email over JMAP, including inbox registration, mailbox listing, message fetching, and sending mail. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atomicmail](https://clawhub.ai/user/atomicmail) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to connect an AI agent to Atomic Mail so it can register an inbox, fetch and triage mailbox data, send replies, and upload attachments through JMAP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores Atomic Mail credentials and JWT bearer tokens locally. <br>
Mitigation: Keep the credentials directory private, exclude it from logs and backups where possible, and never commit credential or JWT files. <br>
Risk: The skill can send email and upload attachments when invoked. <br>
Mitigation: Require explicit user approval before sending mail, replying, forwarding, or uploading attachments through presets or custom JMAP requests. <br>
Risk: Scheduled inbox polling can expose mailbox contents during recurring agent turns. <br>
Mitigation: Use the documented agent-scheduled workflow only in trusted runtimes and avoid raw CLI cron jobs that fetch mail without an agent review step. <br>


## Reference(s): <br>
- [Atomic Mail homepage](https://atomicmail.ai) <br>
- [ClawHub Atomic Mail skill page](https://clawhub.ai/atomicmail/skills/atomicmail) <br>
- [Atomic Mail overview help topic](lib/shared/help/topics/overview.md) <br>
- [Atomic Mail JMAP cheatsheet help topic](lib/shared/help/topics/jmap_cheatsheet.md) <br>
- [OpenClaw cron documentation](https://docs.openclaw.ai/automation/cron-jobs) <br>
- [Hermes cron documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute CLI calls that return JSON JMAP results and write local credential and JWT files during registration.] <br>

## Skill Version(s): <br>
0.3.24 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
