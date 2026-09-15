## Description:

Keyword.com (keyword.com). Use this skill for ANY Keyword.com request \u2014 searching and reading data. Whenever a task involves Keyword.com, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Keyword.com account data through an OOMOL-connected account, including user profiles, projects, regions, keywords, and keyword ranking data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Review installation steps before use and prefer a verified package-manager or manually checked CLI install.

Risk: The skill requires connecting a Keyword.com account through an OOMOL-managed connector.

Mitigation: Use it only when the user trusts OOMOL, understands the connector relationship, and has confirmed the intended Keyword.com connection.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-keyword)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Keyword.com](https://keyword.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before execution and OOMOL-managed credentials for Keyword.com access.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
