## Description:

Gives agents read-only Wikipedia and Wikimedia research tools for articles, media, current events, page history, and public editor activity across multiple languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers and other users can equip agents to research Wikipedia articles, discover Wikimedia media, review article quality and history, and summarize public editor activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public editor activity and article histories can be used to profile contributors.

Mitigation: Use contributor details only when needed for a legitimate research or article-audit task.

Risk: Some tools rely on English-specific content or conventions despite multilingual support.

Mitigation: Check language coverage and verify results against the linked source article.

Risk: The requests dependency is not pinned to an exact version.

Mitigation: Review and pin dependencies in managed deployments.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown text with source and media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include article metadata, public edit history, page-view counts, and image links.]

## Skill Version(s):

1.6.22 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
