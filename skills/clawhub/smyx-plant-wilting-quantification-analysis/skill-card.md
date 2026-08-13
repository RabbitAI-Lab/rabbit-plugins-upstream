## Description:

Analyzes full-plant images or videos to quantify wilting severity, assess likely underwatering or overwatering causes when supporting signals are available, and return structured guidance for plant care workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to evaluate plant wilting from uploaded plant media or URLs, review structured analysis results, and retrieve prior cloud-generated wilting reports. It is intended for smart pots, home gardening, greenhouses, and plant factory monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or media URLs are sent to external Life Emergence cloud endpoints for analysis.

Mitigation: Use only non-sensitive plant media and avoid private URLs unless the publisher documents retention, deletion, and access controls.

Risk: The skill creates or reuses local account/token state for report history with limited user-facing controls.

Mitigation: Deploy only where local identity persistence and cloud report history are acceptable, and document how operators can review or disable that behavior before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis text, with optional saved output files and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return wilting scores, likely cause labels, intervention direction, cloud report history, and exported report links.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
