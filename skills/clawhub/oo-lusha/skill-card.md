## Description:

Operate Lusha through an OOMOL-connected account to search companies and contacts, enrich records, and check account usage with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access Lusha through an OOMOL-connected account for company search, contact search, enrichment, and account usage checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that run scripts directly in a shell.

Mitigation: Install the oo CLI through a trusted, inspectable, versioned method where possible; do not let an agent run installer commands automatically.

Risk: Using the skill routes Lusha data and account access through OOMOL as an intermediary.

Mitigation: Install only when that intermediary is acceptable, and have the user sign in and connect Lusha themselves before agent use.

Risk: Enrichment and account actions can expose contact, phone, email, usage, credit, and plan information.

Mitigation: Inspect each live action schema before running commands and confirm any sensitive payload or effect with the user.

## Reference(s):

- [Lusha Homepage](https://www.lusha.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Lusha Skill](https://clawhub.ai/oomol/skills/oo-lusha)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
