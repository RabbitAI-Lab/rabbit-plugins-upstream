## Description:

Agent自进化Skill helps an agent decide when a solved problem or user preference should be distilled, confirmed by the user, and saved as reusable personal, project, or domain experience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckystar513](https://clawhub.ai/user/luckystar513)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to capture reusable lessons, project-specific pitfalls, domain experience, and user preferences after meaningful problem-solving sessions. It is intended to keep future agent work aligned with confirmed experience rather than unstated assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed memory or profile writes may affect future agent behavior across projects.

Mitigation: Review each proposed lesson or profile update before approval, and modify or reject entries that are too broad, incorrect, or no longer wanted.

Risk: New experience entries may duplicate or conflict with existing stored guidance.

Mitigation: Use the skill's deduplication and conflict-update workflow before saving, and preserve change-log notes when profile preferences are updated.

## Reference(s):

- [Templates and field definitions](references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance and proposed memory/profile entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before saving local experience notes or profile updates.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
