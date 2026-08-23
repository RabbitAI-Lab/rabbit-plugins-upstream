## Description:

Send emails securely without exposing SMTP passwords by using MGC-stored SMTP credentials and scripts that an agent invokes through mgc_run blackbox execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure MGC-backed SMTP workflows where agents can trigger email sending through stored scripts without receiving SMTP credentials. It supports credential setup, script storage, mgc_run invocation, and optional stored email content for stronger privacy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill provides a working pattern for stored script execution that can send real email using persisted SMTP credentials.

Mitigation: Require explicit review before every mgc_run send and use only SMTP credentials the user is comfortable storing in MGC.

Risk: Outbound SMTP automation can send unintended messages if recipient, subject, body, or stored content are not reviewed.

Mitigation: Add recipient allowlists, dry-run mode, and confirmation logging before operational use.

Risk: The security evidence says the skill under-describes runnable automation using stored credentials and outbound SMTP.

Mitigation: Present the security posture plainly during review and require operators to confirm credential storage, script identity, and send parameters before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zkeviny/skills/smtp-sender-secure)
- [MGC Blackbox Repository](https://github.com/zkeviny/MGC-Blackbox)
- [MGC Blackbox Issues](https://github.com/zkeviny/MGC-Blackbox/issues)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown documentation with Python snippets, shell commands, and MGC tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an SMTP script template and mgc_save/mgc_run examples; actual email sending requires MGC, stored credentials, and explicit user approval.]

## Skill Version(s):

2.1.1 (source: release evidence, frontmatter, manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
