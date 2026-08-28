## Description:

Fetches a public web page and produces a structured Markdown digest with the title, key points, entities, action items, and a concise TL;DR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to summarize publicly accessible URLs into quick briefings, key facts, entities, and action items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetching a URL sends the requested page to the agent runtime's web fetch tool, which may be inappropriate for private, paywalled, or sensitive pages.

Mitigation: Use the skill on publicly accessible pages, and avoid sensitive URLs unless the user accepts that the fetch will occur.

Risk: Long pages may be truncated before analysis, which can make the resulting digest incomplete.

Mitigation: Warn when truncation occurs and treat the digest as a partial summary of the fetched content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/page-digest)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses up to 20000 characters of fetched public page content; the digest may be incomplete when source content is truncated.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
