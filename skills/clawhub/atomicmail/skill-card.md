## Description:

Atomic Mail lets an agent register an Atomic Mail inbox and read or send email through JMAP using the bundled CLI, presets, and credential handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[atomicmail](https://clawhub.ai/user/atomicmail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Atomic Mail, register or authenticate an inbox, inspect mailboxes, fetch inbox messages, and send or reply to email when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read inbox contents and send mail through JMAP.

Mitigation: Install it only when agent mail access is intended, review send or reply actions before use, and keep unattended jobs limited to read-only inbox checks.

Risk: Atomic Mail credentials and JWT files grant access to mail capabilities if exposed.

Mitigation: Keep the credential directory private, do not commit or log credentials or JWTs, and use separate credential directories for multi-account setups.

Risk: Scheduled inbox checks may process untrusted email content without a human in the loop.

Mitigation: Review scheduled inbox jobs before enabling them and restrict unattended jobs to the minimum tools needed for read-only message listing.

## Reference(s):

- [Atomic Mail homepage](https://atomicmail.ai)
- [ClawHub skill page](https://clawhub.ai/atomicmail/skills/atomicmail)
- [Atomic Mail publisher profile](https://clawhub.ai/user/atomicmail)
- [SKILL.md](artifact/SKILL.md)
- [JMAP cheatsheet help topic](artifact/lib/shared/help/topics/jmap_cheatsheet.md)
- [Cron help topic](artifact/lib/shared/help/topics/cron.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON JMAP payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the bundled Atomic Mail CLI to produce JMAP request results and registration output.]

## Skill Version(s):

0.3.29 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
