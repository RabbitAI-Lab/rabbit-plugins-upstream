## Description:

Analyzes litter-box area videos or URLs to estimate each cat's litter-box visit frequency and duration, compare behavior with historical baselines, and surface behavior-based urinary health alerts without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, catteries, boarding centers, and veterinary inpatient teams use this skill to review litter-box area videos and generate structured usage statistics for multi-cat health monitoring. The skill is intended to provide behavior-based alerts and report links, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, URLs, report history, internal user identifiers, and account tokens may be sent to or reused with lifeemergence.com services.

Mitigation: Install and run the skill only in workspaces where cloud processing and reuse of these identifiers are acceptable, and review available deletion or credential reset controls before use.

Risk: The skill auto-creates or reuses user identities and persists service tokens in local workspace data.

Mitigation: Use trusted workspaces with appropriate local file access controls, and clear or reset stored credentials when rotating users or moving the workspace.

Risk: Litter-box frequency and duration alerts can be mistaken for medical diagnosis.

Mitigation: Present outputs as behavior statistics and early-warning signals, and direct users to a veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-litter-box-usage-monitor-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON structured reports with usage statistics, alerts, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the report to a local file when an output path is supplied.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
