## Description:

Provides Wikipedia and Wikimedia research tools for article search, summaries, citations, media, readership metrics, and editing history across multiple languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Researchers, writers, and developers use this skill to find and compare Wikipedia articles, examine citations and editing context, and retrieve Wikimedia media or readership information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article queries, locations, and editor usernames or IP addresses are sent to Wikipedia or Wikimedia services.

Mitigation: Avoid sensitive inputs and restrict outbound access to Wikimedia and Wikipedia domains where needed.

Risk: Contributor and IP lookup tools make public editor activity easier to summarize.

Mitigation: Use editor activity summaries responsibly and avoid unnecessary profiling.

Risk: An unpinned requests dependency can change between installations.

Mitigation: Pin and review the requests dependency in controlled deployments.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include article links, source citations, dates, and readership figures, depending on the tool.]

## Skill Version(s):

1.6.24 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
