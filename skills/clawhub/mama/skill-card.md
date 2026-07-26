## Description: <br>
MAMA is a multi-account IMAP/SMTP mail agent for checking accounts, searching and reading messages, handling attachments, drafting replies and forwards, explicitly sending or moving messages, and generating keyword- and deadline-based mailbox digests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hejunhui-73](https://clawhub.ai/user/hejunhui-73) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent perform bounded mailbox workflows across one or more local IMAP/SMTP accounts. It is suited for account checks, message search and reading, draft-based replies or forwards, explicit sends and moves, attachment download, and recurring mail digests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires IMAP/SMTP access and uses local configuration files that can contain mailbox credentials or sensitive preferences. <br>
Mitigation: Install only if mailbox access is acceptable; keep scripts/mail_config.json, any legacy mail_config.py, and digest_config.py private and writable only by trusted users. <br>
Risk: Immediate send, direct forward, and move operations can affect live mailbox contents or send unintended messages. <br>
Mitigation: Prefer draft-generation workflows and use send, forward --send, or move only after reviewing the account, recipient, subject, message body, and target folder. <br>
Risk: Downloaded attachments and stored mail outputs may contain sensitive content or unsafe file types. <br>
Mitigation: Use the default attachment blocking behavior, avoid --allow-risky unless explicitly needed, apply size limits where practical, and clean local .temp outputs according to retention needs. <br>
Risk: Executable local configuration files and generated outputs create review-worthy control gaps noted by the security summary. <br>
Mitigation: Review generated configuration and digest behavior before scheduled or unattended use, and restrict file permissions to trusted users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hejunhui-73/skills/mama) <br>
- [First-run guide](references/first-run-guide.md) <br>
- [Configuration guide](references/config-guide.md) <br>
- [Output format guide](references/output-format-guide.md) <br>
- [Schedule guide](references/schedule-guide.md) <br>
- [Keyword guide](references/keyword-guide.md) <br>
- [Deadline detection guide](references/deadline-detection-guide.md) <br>
- [Channel routing guide](references/channel-routing-guide.md) <br>
- [Troubleshooting guide](references/troubleshooting-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-capable script outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local draft, attachment, cache, summary, and notification files under .temp during use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
