## Description:

Lets agents search and read Wikipedia and Wikimedia content across 10 languages, including article history, citations, media, and readership metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers and other users can retrieve Wikipedia articles, citations, revision history, and Wikimedia media for research and general knowledge tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches require outbound access to public Wikipedia and Wikimedia services.

Mitigation: Allow this access only when appropriate, and avoid sending sensitive queries.

Risk: Returned citations may link to untrusted external sites.

Mitigation: Review off-wiki links before opening them; do not automatically follow them.

Risk: The requests dependency is not pinned to an exact version.

Mitigation: Use a pinned dependency or lockfile in controlled environments.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Plain text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include article links, citations, and media URLs; content varies by tool and language.]

## Skill Version(s):

1.6.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
