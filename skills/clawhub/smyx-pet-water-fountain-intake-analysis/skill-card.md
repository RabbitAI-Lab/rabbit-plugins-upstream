## Description:

Analyzes pet water fountain area videos or URLs through backend APIs to report per-pet drinking frequency, session duration, estimated daily intake, historical baseline changes, and early warning alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet water fountain videos, retrieve structured intake reports, and review historical drinking reports for smart fountains and multi-pet health monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-area videos or URLs, identity values, and usage history may be sent to the configured backend.

Mitigation: Use only when that data transfer is acceptable, review configured endpoints before execution, and disclose backend processing to affected users.

Risk: Tokens may be stored in the workspace data directory.

Mitigation: Limit workspace access, rotate credentials when needed, and provide a deletion process for stored tokens.

Risk: The security evidence says the skill defaults to development HTTP endpoints without enough user control or disclosure.

Mitigation: Switch published configuration to documented HTTPS production endpoints or gate non-production endpoints before deployment.

Risk: Water-intake estimates and alerts can be mistaken for veterinary diagnosis.

Mitigation: Present outputs as health-reference signals only and direct users to veterinary care for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON analysis reports with optional shell command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, historical report tables, status messages, and health-reference warnings.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
