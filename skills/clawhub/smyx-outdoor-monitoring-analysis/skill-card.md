## Description:

Detects targets such as people, vehicles, non-motorized vehicles, and pets within target areas; supports batch image analysis, suitable for outdoor surveillance scenarios like courtyards, orchards, and farms. | 户外看护智能监测分析技能，检测目标区域内的人、车、非机动车、宠物等目标，支持批量图片分析，适用于庭院、果园、养殖场等户外区域看护场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze outdoor monitoring images or videos for people, vehicles, non-motorized vehicles, pets, intrusion signals, risk levels, and historical monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends outdoor images, videos, URLs, account identifiers, and historical monitoring report requests to a Life Emergence backend.

Mitigation: Use the skill only with media and account context that may be shared with that backend, and avoid using it for sensitive locations unless that data flow is acceptable.

Risk: The skill can silently create or reuse an identity, contact account services, and persist tokens in a local workspace SQLite database.

Mitigation: Run it in a separate workspace for sensitive media and review or delete local identity and token data after use when appropriate.

Risk: Outdoor monitoring results are advisory and may be incomplete or incorrect for security decisions.

Mitigation: Treat analysis and risk levels as support for human review, and use professional security procedures for suspicious intrusions or emergencies.

## Reference(s):

- [Skill Page](https://clawhub.ai/18072937735/skills/smyx-outdoor-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON returned from shell-command driven API analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured monitoring results, risk assessments, recommendations, and links to generated or historical reports.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter: 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
