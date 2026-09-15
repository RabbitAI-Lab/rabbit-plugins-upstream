## Description:

lgd-gov-guard maps the LGD Three Laws into government and public-sector AI governance checks for registration, evidence, and gatekeeping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Public-sector AI teams, compliance reviewers, and agent users use this skill to structure local governance self-assessments for AI systems that support decisions, public responses, or data governance. It produces rubric-based registration, evidence, and gatekeeping checks that help identify missing governance artifacts before deployment or release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised one-command installer uses an unpinned npm package with global install scope.

Mitigation: Review the installation path before installing, prefer a fixed reviewed commit or checksum-verified installer, and do not run the global install command with administrator privileges.

Risk: Governance scoring can be mistaken for legal or professional compliance approval.

Mitigation: Use the output as structured self-check guidance and require human review against official current requirements before decisions or release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-gov-guard)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-capable command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local Python script output with exit codes for pass, fail, and usage errors]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
