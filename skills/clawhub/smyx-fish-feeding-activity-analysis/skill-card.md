## Description:

Through built-in cameras of smart feeders or fixed cameras on aquariums, the skill analyzes post-feeding fish videos to estimate gathering, feeding intensity, remaining feed, and a 0-100 feeding activity score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and aquarium or aquaculture operators use this skill to analyze post-feeding video from smart feeders, fixed aquarium cameras, or aquaculture cameras. It returns structured feeding activity reports, alert levels, and non-medication recommendations for follow-up observation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos, URLs, and report history may be tied to an automatically managed cloud identity.

Mitigation: Use the skill only where remote analysis and account-linked history are acceptable, and confirm identity separation and deletion controls before use in shared workspaces.

Risk: The skill stores service tokens locally.

Mitigation: Install and run it only in workspaces where local token storage is acceptable, and review local credential handling before deployment.

Risk: Visual feeding analysis can be unreliable when footage is outside the feeding window, no feeding event is detected, or water clarity is poor.

Mitigation: Treat `feeding_signal_unreliable` as a request to recapture footage, and avoid appetite-decline alerts or operational decisions from unreliable video.

## Reference(s):

- [API 接口文档](references/api_doc.md)
- [smyx_analysis API 接口文档](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured report text or JSON, with Markdown tables for history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include feeding activity score, key submetrics, alert level, recommended actions, next-feeding suggestions, and report links when returned by the service.]

## Skill Version(s):

1.0.13 (source: server release metadata; SKILL.md frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
