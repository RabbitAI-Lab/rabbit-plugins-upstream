## Description:

Resend enables agents to read, send, batch-send, and manage scheduled email through an OOMOL-connected Resend account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to automate Resend email workflows, including listing and retrieving sent or received email, fetching attachment metadata and download URLs, sending individual or batch messages, and updating or canceling scheduled sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include internet installer commands that could execute unreviewed code.

Mitigation: Download the installer separately, verify its source or checksum when available, and review it before execution.

Risk: Resend account and email data are accessed through OOMOL as an intermediary.

Mitigation: Install only when use of OOMOL for the connected Resend account and related email data is acceptable.

Risk: Send, batch-send, cancel, and scheduled-email update actions can change email state or deliver messages.

Mitigation: Confirm exact recipients, payloads, scheduled times, targets, and expected effects before allowing write actions.

## Reference(s):

- [ClawHub Resend Skill](https://clawhub.ai/oomol/skills/oo-resend)
- [Resend Homepage](https://resend.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: evidence release, metadata, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
