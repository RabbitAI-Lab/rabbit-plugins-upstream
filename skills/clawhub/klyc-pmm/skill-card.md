## Description:

KLYC-PMM helps agents persist, search, synchronize, and recover text memory through local shell workflows and HTTPS calls to kunlunyaochi.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to initialize a persistent agent memory profile, push and search text memories, recover memory from a Kunlun recovery URL, and optionally run a watcher that synchronizes selected workspace files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can synchronize sensitive workspace and identity files to kunlunyaochi.com and may run a persistent watcher.

Mitigation: Review the exact files selected for backup or watch mode, limit the scope to intended text memory files, and disable watcher behavior when continuous synchronization is not needed.

Risk: The Kunlun recovery URL functions as a recovery secret.

Mitigation: Store the recovery URL like a password and keep it out of shared memory files, chat logs, screenshots, repositories, and transcripts.

Risk: Memory files may contain API keys, credentials, or other secrets that would be synchronized if included.

Mitigation: Keep credentials out of watched and backed-up memory files, and review memory content before pushing or enabling automatic synchronization.

Risk: The skill includes paid upgrade and payment-link flows.

Mitigation: Require explicit human confirmation of the service tier, price, and payment destination before using any paid upgrade command or generated payment link.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [SkillHub detail page](https://skillhub.cn/skills/syln/kunlunyaochi)
- [KLYC-PMM service page](https://kunlunyaochi.com/?route=klyc-pmm)
- [Security policy](SECURITY.md)
- [PMM full architecture](klyc-pmm-src/references/pmm-full-architecture.md)
- [Pay Skill packaging standard](klyc-pmm-src/references/pay-skill-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local memory, identity, token, index, daemon, and backup files when the user runs the supplied shell commands.]

## Skill Version(s):

9.2.5 (source: frontmatter, skill.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
