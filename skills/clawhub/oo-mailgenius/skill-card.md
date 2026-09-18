## Description:

MailGenius lets an agent operate MailGenius deliverability-audit workflows through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create MailGenius inbound deliverability audits, retrieve pending or completed results, list generated audits, and check daily API test limits from an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts for the oo CLI.

Mitigation: Before installing, verify trust in OOMOL and the oo CLI distribution path; prefer a signed or package-manager installation, or inspect a pinned installer with checksum or signature verification.

Risk: Write actions can create MailGenius audit resources.

Mitigation: Only approve write actions when the exact MailGenius payload and expected effect are clear.

## Reference(s):

- [MailGenius skill on ClawHub](https://clawhub.ai/oomol/skills/oo-mailgenius)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [MailGenius homepage](https://www.mailgenius.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; write actions require user confirmation of payload and effect.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
