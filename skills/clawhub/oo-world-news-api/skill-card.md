## Description:

World News API lets an agent search and retrieve news articles, top-news clusters, sources, and geolocation data through a connected OOMOL account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to ask an agent to search World News API, retrieve articles, find news sources, get top news, or resolve locations while using an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on OOMOL as the broker for World News API access.

Mitigation: Install and use it only when that credential and request brokering model is acceptable for the account and data involved.

Risk: The allowed command permission grants broad oo CLI authority compared with the documented news-read workflow.

Mitigation: Limit execution to the documented world_news_api connector actions and review any requested command before running it.

Risk: The first-time setup guidance includes remote installer commands that pipe scripts into a shell.

Mitigation: Prefer a verified or package-manager installation path for the oo CLI, or inspect the installer before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-world-news-api)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [World News API homepage](https://worldnewsapi.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live World News API response data returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
