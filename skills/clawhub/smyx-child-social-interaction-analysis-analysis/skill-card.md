## Description:

Analyzes video from early childhood settings to summarize children's social interactions, including approaches, conversations, and cooperative play.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and early childhood staff use video-based interaction counts, durations, initiator summaries, and heatmaps to inform classroom observation and follow-up. The results are behavioral summaries and do not provide psychological or developmental diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's video is sent to a cloud analysis service, while upload, retention, account separation, and credential protections are unclear.

Mitigation: Before using real footage, require clear provider terms for uploads, retention, account separation, and token protection; obtain guardian and institution authorization, and use an isolated workspace.

Risk: The --export-env-only option is ignored, so it does not prevent an analysis from running.

Mitigation: Do not rely on this option as a safeguard; use only a version verified to stop before analysis when the option is set.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Report links]

**Output Format:** [Markdown summary and structured JSON with interaction counts, durations, initiators, and available heatmap or report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video-based estimates; results are directional educational references, not diagnoses.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
