## Description:

World News API (worldnewsapi.com). Use this skill for ANY World News API request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query World News API through an OOMOL-connected account for article search, article retrieval, top-news discovery, source search, and location lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes piping a remote installer directly into a shell.

Mitigation: Prefer a signed or package-manager installation for the oo CLI; if using the installer, review it first and pin or verify the downloaded content where possible.

Risk: The skill routes World News API access through an OOMOL-connected account.

Mitigation: Connect only the account and scopes intended for agent use, and review authentication or connection prompts before proceeding.

## Reference(s):

- [World News API Homepage](https://worldnewsapi.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-world-news-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and returns World News API response data through the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
