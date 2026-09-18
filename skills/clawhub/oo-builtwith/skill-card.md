## Description:

BuiltWith helps agents inspect live connector schemas and retrieve BuiltWith domain technology profiles, summaries, recommendations, redirect history, and social-profile matches through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query BuiltWith data through the OOMOL `oo` CLI for domain technology intelligence, recommendations, redirect history, and social-profile domain matches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands executed directly in a shell.

Mitigation: Review the setup path before installing; use the skill for BuiltWith lookups only and avoid remote installer commands unless the OOMOL distribution path and installer are independently verified.

## Reference(s):

- [ClawHub BuiltWith Skill](https://clawhub.ai/oomol/skills/oo-builtwith)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented BuiltWith connector actions; responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
