## Description:

Analyzes crop leaf, bud, or fruit images and videos by calling server-side APIs to identify common agricultural pests such as aphids, red spider mites, cotton bollworms, and corn borers with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, and agronomy support teams use this skill to analyze crop images or videos for early pest identification, structured findings, confidence scores, and report links. It supports pest observation workflows but does not provide pesticide or treatment recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crop images, videos, or URLs are sent to provider-operated APIs and may be associated with an implicit identity.

Mitigation: Use only media appropriate for the provider service, avoid unrelated sensitive imagery, and confirm API configuration, retention, and access controls before broad use.

Risk: The skill may silently create or reuse a remote account and store tokens in a local SQLite database.

Mitigation: Run it in a controlled workspace, protect local data directories, remove stored tokens when no longer needed, and ask the publisher to document authentication and token storage behavior.

Risk: The authoritative security verdict is suspicious because the skill combines real pest analysis with silent identity use and local token storage.

Mitigation: Review the security summary and install only after accepting those operational risks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API interface documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands]

**Output Format:** [Markdown or JSON-formatted structured pest analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes pest types, estimated counts, confidence scores, and report or export links; supports local image/video files and media URLs.]

## Skill Version(s):

1.0.8 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
