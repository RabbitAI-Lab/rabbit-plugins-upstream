## Description:

Sherpa helps agents retrieve personalized travel restrictions, document requirements, and concise travel or visa summaries through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Sherpa travel restriction and document requirement lookups. It supports trip detail retrieval and concise Markdown travel or visa summaries after Sherpa is connected through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running remote installer scripts that could execute arbitrary code if the delivery source is compromised.

Mitigation: Use the skill for Sherpa read lookups only until the OOMOL CLI installer is independently trusted; prefer a signed or package-manager install path, verify the installer where possible, and avoid elevated shells.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sherpa)
- [Sherpa Homepage](https://www.joinsherpa.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
