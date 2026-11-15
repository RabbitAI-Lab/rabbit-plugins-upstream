## Description:

Retrieves details and engagement metrics for individual Weibo posts to support content research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve a Weibo post's content, author, publication time, media, and engagement counts for content research and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly invokes an automatically installed, unpinned CLI package, so the code may change without review; the security verdict is suspicious and scanner coverage is partial.

Mitigation: Review the CLI package and its versioning before installing or running it, especially before entering an API key.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON with concise factual summaries when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Post details and available media and interaction fields; optional local media-save instructions.]

## Skill Version(s):

0.1.22 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
