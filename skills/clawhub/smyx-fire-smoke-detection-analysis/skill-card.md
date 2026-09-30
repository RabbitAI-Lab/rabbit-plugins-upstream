## Description:

Analyzes images and video for signs of fire and smoke and returns detection reports for early-warning workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security teams, site operators, and developers can analyze surveillance footage or images for possible fire and smoke and review detection reports or historical results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, URLs, and identity-linked metadata may be sent to lifeemergence.com services, including sensitive surveillance footage or private URLs.

Mitigation: Use only approved media and URLs after reviewing the provider's data handling; avoid sensitive footage and private/internal URLs without authorization.

Risk: The skill creates a persistent local database containing user identity and service tokens.

Mitigation: Review the skill before installation and protect access to the local database and stored service tokens.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fire-smoke-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured detection reports, JSON results, report links, or Markdown tables of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fire and smoke indicators, risk levels, detected regions, and report links.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; bundled SKILL.md states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
