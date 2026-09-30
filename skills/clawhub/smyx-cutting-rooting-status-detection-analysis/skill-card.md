## Description:

Analyzes images or videos of plant cuttings in transparent containers to detect visible root primordia or early roots, classify rooting stage, and return transplant-timing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and propagation teams use this skill to monitor cutting-rooting progress from transparent-container images or videos without disturbing the plant. It reports rooting stage, visible root-point distribution, rough early-root development, and related management suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, and report metadata are sent to the lifeemergence.com cloud service for analysis.

Mitigation: Use only media that is acceptable to process with that third-party cloud service, and avoid including sensitive background details in submitted images or videos.

Risk: The skill can create or reuse local identity state and store service tokens in a workspace SQLite database.

Mitigation: Avoid shared workspaces unless operators understand how to clear the workspace data directory and revoke related service-side session or account state.

Risk: Rooting-stage outputs are visual assessments and may be affected by container glare, water spots, lighting, or occluded roots.

Mitigation: Treat results as propagation-management guidance and verify important transplant decisions with repeat observations or direct inspection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cutting-rooting-status-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [Shared API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text containing structured JSON-like analysis results and report links; optional output file writes the same text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video paths or public media URLs; history queries return structured report-list text from the cloud service.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
