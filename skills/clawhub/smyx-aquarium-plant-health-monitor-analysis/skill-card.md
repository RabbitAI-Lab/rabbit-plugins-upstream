## Description:

Analyzes aquarium plant images and videos for visible health issues and provides a health assessment with care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquascapers, and aquarium shop staff can use the skill to assess visible plant health issues from aquarium images or videos and get care direction. Its assessment is visual and does not provide specific water chemistry targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags account registration, local token storage, and external media processing as concerns beyond the stated aquarium plant health purpose.

Mitigation: Before use, confirm what identity information and media are sent, where credentials are stored, and whether export-only mode can trigger analysis. Proceed only if comfortable with those behaviors.

Risk: The security scan was partial because a referenced local path could not be resolved, leaving some behavior unverified.

Mitigation: Review the unresolved behavior before installing or using the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis text or JSON, with a report export link when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual assessments may be uncertain and are not a substitute for water testing or expert advice; no specific water chemistry targets are provided.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata; artifact frontmatter says 1.0.23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
