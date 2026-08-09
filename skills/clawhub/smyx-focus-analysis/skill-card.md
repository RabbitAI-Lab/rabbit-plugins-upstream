## Description:

Real-time detection of gaze direction and facial pose to quantify states of focus, distraction, or mind-wandering for classroom learning, office meetings, and driving attention monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze videos or video URLs for attention, distraction, and mind-wandering signals. It can return structured focus reports, historical report listings, recommendations, and report links for classroom, office, or driving contexts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive videos, video URLs, and report activity may be sent to configured external services.

Mitigation: Use only with appropriate consent and data-handling approval, especially for classroom, workplace, or driving footage.

Risk: The skill can silently create or reuse identity state and store local identity or token data in the workspace.

Mitigation: Run it in a controlled workspace, review stored identity/token files before reuse, and clear local state when the analysis context changes.

Risk: Focus-analysis reports may be interpreted as definitive assessments of people.

Mitigation: Treat results as decision support only and require human review before taking educational, employment, safety, or operational action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-focus-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration]

**Output Format:** [Markdown or JSON analysis reports, with optional saved text output and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or video URLs; supported formats are mp4, avi, and mov with a documented 10 MB file-size limit.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
