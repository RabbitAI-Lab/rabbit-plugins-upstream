## Description:

Requests cloud-based video analysis for condensed time-lapse albums and returns reports or account-linked report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People organizing home videos, travel footage, or event recordings use the skill to request condensed album analysis from a local video or URL and review reports or previous results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local videos and submitted URLs may be sent to lifeemergence.com services.

Mitigation: Use only media and URLs that may be shared with the service; avoid sensitive videos and private or signed links.

Risk: The skill may create or reuse a local account identity and store service tokens for account-linked report history.

Mitigation: Review local identity and token storage before installation, and use an appropriate account or isolated workspace.

Risk: The advertised keyword or target description is not forwarded to the analysis call in this version.

Mitigation: Do not rely on keyword filtering; check results against the requested target before using them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-custom-timelapse-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis reports, report links, and Markdown history lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be account-linked; keyword-based targeting is unreliable in this release.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release metadata; artifact frontmatter says 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
