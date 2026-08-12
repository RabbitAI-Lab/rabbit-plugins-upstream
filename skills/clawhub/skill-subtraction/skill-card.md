## Description:

Audits installed AI skills, classifies them by value and relevance, and generates structured keep, archive, or uninstall recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[helloyxs](https://clawhub.ai/user/helloyxs)

### License/Terms of Use:

MIT

## Use Case:

Developers and AI assistant users use this skill to audit installed skills, reduce clutter, and decide which skills to keep, archive, or uninstall. It is useful for periodic skill inventory reviews, project transitions, or cleanup after accumulated skill installations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner inspects local skill directories and reports installed skill metadata.

Mitigation: Run it only in environments where local skill inventory disclosure is acceptable, and use broader scan flags such as --all or --workspace only intentionally.

Risk: Cleanup recommendations may lead to archiving or uninstalling skills the user still needs.

Mitigation: Review the generated keep, archive, and uninstall recommendations before acting; the skill documentation describes cleanup as requiring explicit user confirmation.

Risk: Filesystem permission or malformed skill metadata can make the audit incomplete.

Mitigation: Check the scanner's issues field and stderr summary before relying on the report.

## Reference(s):

- [Evaluation Framework](references/evaluation_framework.md)
- [ClawHub skill page](https://clawhub.ai/helloyxs/skills/skill-subtraction)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance]

**Output Format:** [Markdown audit report with optional JSON output from the bundled Python scanner]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The scanner reports local skill metadata and issues; cleanup actions are described as confirmation-gated.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
