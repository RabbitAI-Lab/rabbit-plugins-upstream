## Description:

Quantifies plant wilting severity from full-plant images or videos and optionally uses soil-moisture context to distinguish underwatering from waterlogging for smart pots, home gardening, greenhouses, and plant factories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit plant images, videos, or URLs for cloud analysis that returns structured wilting severity, likely underwatering or waterlogging cause, intervention guidance, history records, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media, media URLs, and report history are sent to lifeemergence.com services for analysis and lookup.

Mitigation: Use only plant media and URLs that are approved for that external service, and avoid images or videos that expose sensitive surroundings or metadata.

Risk: The skill can silently create or reuse an account-like identifier and store authentication tokens in the workspace data directory.

Mitigation: Run it in a workspace appropriate for that service identity, protect the workspace data directory, and remove stored credentials or tokens before sharing the workspace.

Risk: Wilting cause and intervention guidance can be wrong when imagery is unclear or soil-moisture context is absent.

Mitigation: Confirm soil moisture and plant condition manually before acting on watering or drainage guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [smyx_analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown and JSON-formatted structured report text with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and history-query tables; detail modes include basic, standard, and json.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
