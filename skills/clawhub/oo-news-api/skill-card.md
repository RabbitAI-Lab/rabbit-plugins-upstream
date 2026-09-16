## Description:

News API (newsapi.org) connector for searching and reading News API data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query News API through an OOMOL-connected account for article search, top headlines, breaking headlines, and source metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Review installation steps before use and prefer an official package manager or a pinned, signed release with checksum or signature verification.

Risk: The skill depends on an authenticated OOMOL connection for News API access.

Mitigation: Run normal News API actions only after the oo CLI is installed, authenticated, and connected to the expected News API account.

## Reference(s):

- [News API homepage](https://newsapi.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-news-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal actions return JSON from the OOMOL connector under a data object with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
