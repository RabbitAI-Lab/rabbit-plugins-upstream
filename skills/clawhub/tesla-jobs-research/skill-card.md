## Description:

Researches Tesla job postings through the Crawlora API, letting an agent search Tesla careers by title, department, or location and retrieve full posting details by job id as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, recruiters, job seekers, and developers use this skill to search public Tesla job openings and retrieve complete posting details through Crawlora's Tesla Jobs endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tesla job search queries and the Crawlora API key are sent to Crawlora when the helper is used.

Mitigation: Use the skill only when that external API use is acceptable, keep CRAWLORA_API_KEY in the environment, and do not hardcode or commit the key.

Risk: The skill requires shell and network access to call the Crawlora API helper.

Mitigation: Grant shell and network permission only for the provided helper and review commands before execution.

## Reference(s):

- [Tesla Jobs endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/tesla-jobs-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses fixed Crawlora Tesla Jobs endpoints.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
