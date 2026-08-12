## Description:

Uses pet facial image or video input to identify a pet, query linked vaccination records, compare the last dose date against the reminder cycle, and return due or overdue vaccination reminders without providing medical advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet hospitals, boarding centers, and pet-insurance workflows can use this skill to check whether a recognized pet appears due or overdue for vaccination based on linked records. It is intended for database-comparison reminders, not veterinary diagnosis or medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet media and report queries to lifeemergence.com cloud services.

Mitigation: Use only when users have authority to upload the pet image or video and query the linked vaccination records.

Risk: The skill silently creates or reuses an internal identity and stores service tokens locally in the workspace data path.

Mitigation: Install only in workspaces where persistent local credentials are acceptable, and review or clear stored identity data according to local policy.

Risk: The output is based on database comparison and facial recognition matching, not medical judgment.

Mitigation: Treat reminders as administrative prompts and route vaccination decisions to qualified veterinary staff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown or JSON text containing a structured analysis result, due or overdue reminder status, and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud history and return report lists or exported report URLs.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
