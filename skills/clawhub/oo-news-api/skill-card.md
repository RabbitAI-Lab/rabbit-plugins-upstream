## Description:

News API lets agents search and read News API content through OOMOL's news_api connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search published articles, retrieve top headlines, list news sources, and request legacy source-based article results through an OOMOL-connected News API account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell and PowerShell installer commands that could execute unverified code if run automatically.

Mitigation: Install the oo CLI manually from a trusted, verified source and do not allow an agent to run curl-to-bash or PowerShell installer commands automatically.

Risk: The connector uses an OOMOL-connected account, so actions may depend on account access, billing status, and intentionally connected News API credentials.

Mitigation: Sign in and connect News API only when the user explicitly intends to use this connector, and stop on billing or connection errors until the user resolves them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-news-api)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [News API Homepage](https://newsapi.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return News API response data as JSON with execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
