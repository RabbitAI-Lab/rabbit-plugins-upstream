## Description:

Release Gate Audit helps agents decide whether a repository or artifact is ready for public release by auditing git-tracked files and history for credentials, organization-internal information, PII, and local-only artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, release engineers, and compliance reviewers use this skill before open-sourcing, external sharing, or release approval to check the public-facing git surface and verify remediation of sensitive findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated audit reports and organization term files can contain secrets, internal identifiers, or sensitive excerpts.

Mitigation: Keep reports and organization term files private, avoid committing them publicly, and use gitignore or equivalent controls for local-only evidence.

Risk: Automated scanner findings are leads rather than final conclusions.

Mitigation: Manually review P0/P1 findings with the playbook, revoke valid credentials before cleanup, and verify remediation with before/after reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/release-gate-audit)
- [False Positive Playbook](references/false-positive-playbook.md)
- [Threat Categories](references/threat-categories.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON/text audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces release gate decisions, categorized findings, remediation guidance, and verification checklists when the bundled scripts are run.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
