## Description:

Compliance expert for snyk-agent-scan, focused on restructuring agent skill files to address W001, W011, and W012 scanner alerts without suppressing useful information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this agent skill to remediate snyk-agent-scan findings in SKILL.md, references, assets, and secondary Markdown files. It is intended for authoring new skills, editing existing skills, triaging local or CI scanner failures, and unblocking pull requests held by agent scanner alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may recommend moving install instructions into metadata or frontmatter, making risky dependency or tool changes less visible in the body text.

Mitigation: Review metadata, install blocks, allowed tools, and dependency versions before accepting changes; verify package provenance and pin versions where possible.

Risk: Scanner remediation may alter skill behavior or omit useful context if edits are accepted without review.

Mitigation: Review every proposed content change and rerun snyk-agent-scan after each remediation step to confirm the alert count and behavior changed as intended.

Risk: The scanner requires SNYK_TOKEN, which could be exposed if used in untrusted local or CI contexts.

Mitigation: Keep SNYK_TOKEN limited to trusted local environments or CI secret stores and avoid printing it in command output or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/snyk-agent-scan-compliance)
- [cc-skills repository](https://github.com/samber/cc-skills)
- [W001 pattern catalog](references/w001-patterns.md)
- [W011 pattern catalog](references/w011-patterns.md)
- [W012 pattern catalog](references/w012-patterns.md)
- [snyk-agent-scan issues](https://github.com/snyk/snyk-agent-scan/issues)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell examples, and YAML frontmatter snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to skill metadata, install blocks, allowed tools, dependency versions, and scanner remediation text.]

## Skill Version(s):

1.1.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
