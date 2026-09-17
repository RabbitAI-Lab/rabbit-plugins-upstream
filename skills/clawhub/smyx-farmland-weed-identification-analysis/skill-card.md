## Description:

Identifies weed species and coverage density from field top-view images, and outputs a weed distribution heatmap dataset to support precision weeding decisions. | 通过田间图像识别杂草种类与覆盖密度，生成除草建议区域热力图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External agricultural users and farm operations teams use this skill to analyze field top-view images or videos for weed species, weed coverage density, distribution areas, heatmap data, and report links that support precision weeding decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan verdict is suspicious because identity, credential, persistence, HTTP transport, and payment-workflow behaviors need review before installation.

Mitigation: Review the skill before installing and do not use real farm media, API keys, or account-linked histories until the publisher documents and hardens those behaviors.

Risk: The artifact resolves or creates an internal user identity and stores token-related user records locally for API calls and report history.

Mitigation: Require clear user-visible identity controls and move tokens or account-linked state to a protected secret store before production use.

Risk: The bundled configuration includes HTTP endpoints and a remote API workflow for analysis, report listing, and report export.

Mitigation: Use an HTTPS production configuration and verify endpoint ownership before processing real farm media or account-linked report history.

Risk: A 402 API response can direct the user toward a separate payment skill workflow.

Mitigation: Confirm the payment workflow, publisher, and billing terms out of band before following payment-related instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a file when an output path is supplied; report-list output is formatted from API-returned records.]

## Skill Version(s):

1.0.11 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
