## Description:

DiscoLike lets agents search and read DiscoLike company intelligence through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover companies and retrieve DiscoLike business profiles, growth metrics, SSL certificate metrics, digital footprint scores, and usage counters through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes remote installer commands that run scripts directly without built-in verification.

Mitigation: Do not let an agent run first-time installer commands automatically; install the oo CLI only through a trusted, verifiable method, preferably with a pinned release and signature or checksum verification.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-discolike)
- [DiscoLike Homepage](https://discolike.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload or response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call DiscoLike read actions through the OOMOL-connected oo CLI; no raw API credentials are handled by the agent.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
