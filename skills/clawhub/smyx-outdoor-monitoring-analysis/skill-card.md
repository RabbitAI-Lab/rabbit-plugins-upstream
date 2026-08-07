## Description:

Detects targets such as people, vehicles, non-motorized vehicles, and pets within target areas; supports batch image analysis, suitable for outdoor surveillance scenarios like courtyards, orchards, and farms. | 户外看护智能监测分析技能，检测目标区域内的人、车、非机动车、宠物等目标，支持批量图片分析，适用于庭院、果园、养殖场等户外区域看护场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze outdoor camera images, videos, or public media URLs for people, vehicles, non-motorized vehicles, and pets. It returns structured monitoring reports, report links, and history listings for outdoor care scenarios such as courtyards, orchards, farms, and breeding areas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted outdoor images, videos, and report-history queries are processed by configured cloud services.

Mitigation: Use the skill only for media whose privacy, retention, account, and deletion controls are acceptable for the deployment.

Risk: The skill can create or reuse a persistent local or remote identity and stored tokens for report history.

Mitigation: Review account and token handling before installation, and prefer dedicated accounts or environments for sensitive monitoring workflows.

Risk: Monitoring results are security-support information and may be incomplete or incorrect.

Mitigation: Use human review for consequential decisions and follow the skill guidance to contact appropriate responders for suspicious intrusions.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-outdoor-monitoring-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown text with embedded structured JSON and report links; optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video paths or public media URLs; supports history-list queries.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter lists 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
