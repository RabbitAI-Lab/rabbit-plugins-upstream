## Description:

AI-powered succulent special-state detection from HD images via plant cameras or smartphones that identifies black rot, leaf melting, and stretching, then reports the anomaly type, severity grade, and confidence for home succulent care, greenhouses, and flower shops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze succulent plant images or videos for three special states: black rot, leaf melting, and stretching. It can return structured reports, confidence values, severity grading, report links, and history lookups for care workflows in homes, greenhouses, and flower shops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded images, videos, or media URLs may be sent to a remote analysis service and associated with a persistent identity.

Mitigation: Use only media that is appropriate for remote processing, confirm the service endpoint and retention expectations, and avoid submitting sensitive images or URLs.

Risk: The skill stores or reuses local identity and token state for analysis and history lookup.

Mitigation: Review local storage behavior before installation and rotate or remove persisted credentials when changing users or environments.

Risk: Development configuration includes HTTP and private-IP service defaults.

Mitigation: Replace development endpoints with approved production HTTPS endpoints before operational use.

## Reference(s):

- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with status, severity, confidence, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local image or video paths, remote media URLs, optional output files, basic/standard/json detail levels, and cloud-backed history list output.]

## Skill Version(s):

1.0.14 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
