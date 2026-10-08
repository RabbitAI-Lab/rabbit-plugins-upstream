## Description:

Identifies a pet from an image or video and compares its vaccination records with the configured reminder interval to report doses that may be due or overdue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet hospital staff and other pet-care providers use pet images or videos to check linked vaccination records, receive due-date reminders, and review prior reports. Results are record-based reminders, not veterinary advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared fallback identity and locally stored tokens may expose sensitive report or history access across users.

Mitigation: Use only in a single-user or isolated workspace until authenticated per-user identity, scoped report access, and protected token storage are in place.

Risk: Pet media, generated reports, and report links contain sensitive information processed by a cloud service.

Mitigation: Share and retain inputs and links only as appropriate for sensitive data; review cloud processing before use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [Skill API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured vaccination reminder results, report links, or a Markdown history table; optional JSON or saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports compare stored vaccination dates with a configurable reminder interval; they do not provide veterinary advice.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled SKILL.md states 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
