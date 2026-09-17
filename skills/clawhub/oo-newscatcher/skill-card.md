## Description:

NewsCatcher helps agents search and read NewsCatcher data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve recent headlines, search global news articles, list indexed sources, and check subscription details from a connected NewsCatcher account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI only from a trusted and verified source, and require explicit review before running curl-to-bash or irm-to-iex setup commands.

## Reference(s):

- [ClawHub NewsCatcher Skill Page](https://clawhub.ai/oomol/skills/oo-newscatcher)
- [NewsCatcher Homepage](https://www.newscatcherapi.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running NewsCatcher read actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
