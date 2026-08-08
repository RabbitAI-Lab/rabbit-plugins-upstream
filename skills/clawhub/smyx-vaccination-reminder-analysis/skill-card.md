## Description:

Analyzes pet face images or videos to match a registered pet, compare vaccination records against the configured reminder cycle, and return due or overdue vaccination reminders without providing medical advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet hospitals, boarding centers, and insurance workflows use this skill to check whether a recognized pet is due or overdue for vaccination based on stored records. It supports operational reminders and record lookup, not veterinary diagnosis or medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media, identifiers, vaccination records, and report data may be sent to configured lifeemergence cloud services.

Mitigation: Use only in workflows where this data transfer is approved and where consent, retention, deletion, and authorization requirements are documented.

Risk: The skill can silently create or reuse identities and store tokens locally.

Mitigation: Review identity handling and local credential storage before installation, and restrict use to environments where this behavior is approved.

Risk: Cloud report-history retrieval has limited user control.

Mitigation: Confirm that users and operators understand what history can be retrieved and who is authorized to access it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown reports and tables, with JSON available for detailed output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vaccination reminder status, report links, and history-list tables.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
