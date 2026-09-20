## Description:

出行保障助手为旅行者提供旅行保险方案推荐、保障条款白话解读和理赔流程指引。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to compare travel-insurance coverage, understand policy terms, and prepare claim steps for common trip scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because it requests PROXY_TOKEN while describing itself as a local, no-API-key skill that does not transmit personal information.

Mitigation: Review before installing and require the publisher to remove the credential declaration or clearly document why it is needed and what data it can access.

Risk: Insurance recommendations and claim guidance may be incomplete or differ from official policy terms.

Mitigation: Treat output as informational guidance and verify coverage, exclusions, claim deadlines, and purchase terms with the insurer or platform before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/travel-insurance-smart-buy)
- [Publisher profile: travel-skills](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style Chinese text with scenario sections, recommendations, links, checklists, and step-by-step guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns local knowledge-base guidance; does not directly sell insurance, process payments, or determine claim outcomes.]

## Skill Version(s):

2.0.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
