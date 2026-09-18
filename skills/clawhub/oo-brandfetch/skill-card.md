## Description:

Use Brandfetch through an OOMOL-connected account to search and read brand data instead of calling the Brandfetch API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch Brandfetch brand profiles and resolve transaction labels through the OOMOL-connected Brandfetch connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer commands that execute local code without local verification.

Mitigation: Review the oo CLI installation path first, prefer official version-pinned or inspectable installer packages, and run remote shell installers only when OOMOL's installer infrastructure is trusted.

Risk: Brandfetch connector action contracts can change over time.

Mitigation: Fetch the live connector schema before each run and build payloads only from the current schema.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-brandfetch)
- [Brandfetch Homepage](https://brandfetch.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Brandfetch connector schemas before each run; OOMOL keeps credentials server-side.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
