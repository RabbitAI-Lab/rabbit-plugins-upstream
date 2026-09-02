## Description:

Reviews structured .xlsx cutover manuals for application cloud migration and big-data stack migration, checking maintenance notices, traffic switching, source database read-only and session handling, Alibaba Cloud application restart strategy, and rollback decision conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, migration engineers, SREs, DBAs, and operations teams use this skill to review .xlsx cutover manuals before cloud migration events and generate rule-based risk findings with remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain sensitive infrastructure details from the reviewed cutover manual.

Mitigation: Keep reports in a controlled local directory, use the default redaction behavior, and avoid --no-redact unless the output will be protected.

Risk: The review is based on rule matching and keyword detection, so scores and findings may miss business-specific context.

Mitigation: Treat the report as decision support only and require human review, remediation validation, rehearsal, and expert approval before executing a cutover.

Risk: Unexpected customer PII in a cutover manual may not be fully covered by the ops-focused redaction patterns.

Mitigation: Manually inspect reports before external sharing and remove or protect any unexpected PII.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/sdk-team/skills/alibabacloud-migration-cas-cutover-review)
- [Installation and Usage Guide](references/usage-guide.md)
- [Review Standard](references/review-standard.md)
- [RAM Permission Declaration](references/ram-policies.md)
- [Version History](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON reports with scored findings, severity labels, and remediation recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local .xlsx cutover manuals and writes local reports; default review covers the cutover execution and rollback Sheets unless additional Sheet types are explicitly requested.]

## Skill Version(s):

0.0.1-beta.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
