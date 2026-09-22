## Description:

文档扫描增强 helps agents send a single document image to a scanning service for enhancement, cleanup, correction, and style-conversion workflows across 13 supported scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to enhance or clean up one static document image at a time, including exams, receipts, contracts, screenshots, watermark removal, shadow removal, background cleanup, crop correction, sketch conversion, and line-art extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote image processing can expose document contents to an external scanning service.

Mitigation: Use only documents appropriate for that service, avoid sensitive personal or business data unless the service is trusted, and rotate the scanning service key if it is exposed.

Risk: Watermark removal and exam-answer removal workflows can be misused to strip attribution, bypass rights, or alter assessment materials deceptively.

Mitigation: Limit these workflows to authorized cleanup, restoration, or accessibility use cases where the user has rights to modify the image.

Risk: Overbroad activation text and command execution examples can lead an agent to run the skill outside the intended document-image cleanup task.

Mitigation: Review the requested scene and command before execution, and allow only the documented scene identifiers and single-image inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/alibaba-quark-scan)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and JSON-style execution results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes one static image per request; successful image outputs may be saved as temporary local files.]

## Skill Version(s):

1.0.3 (source: server release evidence and target metadata; artifact frontmatter lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
