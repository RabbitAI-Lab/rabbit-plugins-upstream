## Description:

Accurately identifies cat and dog breeds and supports distinguishing between different individuals in multi-pet households.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze pet images, videos, or URLs for cat and dog breed identification, individual pet distinction in multi-pet households, confidence details, and report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet photos, videos, or supplied URLs are sent to the publisher's remote service.

Mitigation: Use only media you are comfortable sharing with the publisher's service, and avoid sensitive household media unless retention and transport details are clarified.

Risk: Report history is associated with an internal identity that the skill can create or reuse silently.

Mitigation: Review the identity behavior before installation and ensure users understand that history lookup is tied to that internal identity.

Risk: A local SQLite database may store account tokens.

Mitigation: Install only in environments where local token storage is acceptable, and protect or periodically clear the workspace data store according to local policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-breed-individual-recognition-analysis)
- [Pet breed individual recognition API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Markdown or JSON analysis reports, Markdown report-history tables, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image or video paths, public media URLs, detail-level selection, report-list requests, and optional output file paths.]

## Skill Version(s):

1.0.11 (source: server release metadata; SKILL.md frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
