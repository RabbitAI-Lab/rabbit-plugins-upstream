## Description:

Meituan lets agents query Meituan travel information through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Meituan travel data for flights, trains, hotels, attractions, itineraries, and local transportation. The skill guides agents to inspect live connector schemas before running read-oriented travel queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may run mutable remote installer scripts without verification.

Mitigation: Install only after reviewing official OOMOL installation instructions, prefer a pinned or verifiable installer when available, and approve login or connection steps manually.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-meituan)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Meituan Homepage](https://www.meituan.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a caller timeout longer than 120 seconds for travel queries.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
