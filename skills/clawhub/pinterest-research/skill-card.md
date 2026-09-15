## Description:

Researches public Pinterest profiles, boards, pins, Ideas categories, and search results through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to inspect public Pinterest profiles, boards, pins, category feeds, and keyword search results for content research, competitor audits, and trend scouting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pinterest lookup terms, usernames, board slugs, pin IDs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only for intended public Pinterest research, avoid sensitive or private queries, and provide the API key through CRAWLORA_API_KEY rather than hardcoding it.

## Reference(s):

- [Pinterest endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/pinterest-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public Pinterest data returned by Crawlora; list endpoints may require pagination.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
