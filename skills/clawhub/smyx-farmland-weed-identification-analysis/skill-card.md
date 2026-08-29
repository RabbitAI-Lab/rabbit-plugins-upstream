## Description:

Identifies weed species and coverage density from field top-view images, and outputs a weed distribution heatmap dataset to support precision weeding decisions. | 通过田间图像识别杂草种类与覆盖密度，生成除草建议区域热力图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural operators, agronomy teams, and agent users can use this skill to analyze field images or videos for weed species, coverage density, distribution areas, pressure level, heatmap data, and report links. It is intended to support precision weeding decisions, not to provide herbicide or treatment recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends field images or videos and identity-linked requests to the provider backend.

Mitigation: Use only media that is appropriate to share with the provider, and confirm data retention, access, and deletion practices before production use.

Risk: The skill creates or reuses a local identity and stores authentication tokens in a workspace SQLite database.

Mitigation: Run the skill in an isolated workspace, protect the workspace data directory, and remove or rotate stored credentials when access is no longer needed.

Risk: The security evidence reports development HTTP endpoint configuration.

Mitigation: Ask the publisher to ship production HTTPS endpoint configuration and verify endpoint settings before installation.

Risk: History lookups can retrieve reports associated with the current identity.

Mitigation: Require clear user confirmation before report-history queries and avoid exposing report links outside the intended user context.

## Reference(s):

- [Farmland weed analysis API reference](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured text or JSON analysis output, with Markdown tables for history listings and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns weed species, coverage density, distribution areas, pressure level, heatmap data, and report links when available.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; artifact frontmatter states 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
