## Description:

Estimates an indoor plant's relative transpiration rate from thermal or RGB leaf media plus environmental data and returns water-stress, root-activity, and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, plant-care operators, and greenhouse researchers use this skill to estimate transpiration rate, root water-uptake activity, and likely environmental stress from plant leaf images or video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads plant images or videos and related identifiers to the publisher's remote services.

Mitigation: Use non-sensitive media, review what files or URLs are submitted, and confirm the publisher's retention and opt-in controls before use.

Risk: The skill can silently create or reuse account identity and store reusable session tokens in a local workspace database.

Mitigation: Run it in a controlled workspace, avoid sharing the workspace database, and prefer safer token storage or explicit credential handling before production deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-transpiration-rate-estimation-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API 接口文档](artifact/references/api_doc.md)
- [API接口文档](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown or JSON analysis report with optional report links and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the report output to a user-selected local file when requested.]

## Skill Version(s):

1.0.9 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
