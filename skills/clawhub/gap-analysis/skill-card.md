## Description:

Audits repositories for evidence-backed gaps between code, SPECs, architecture, and documentation, then prepares Draft SPECs, GitHub issue plans, and orchestrator handoffs behind an explicit approval gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before releases, after reviews, or during repository audits to compare implemented behavior against documented requirements and produce evidence-backed remediation work. It is intended for artifact analysis and planning, not evaluation of people or team performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository-wide audit access can expose sensitive project files, local agent memory, Git state, and GitHub issue metadata.

Mitigation: Run the skill only in workspaces intended for audit, keep sensitive data out of local memory files, and redact secrets or personal data in reports and generated work items.

Risk: Git remote URLs or local metadata may contain credentials or other sensitive values.

Mitigation: Remove credentials from Git remote URLs before use and record only redacted path and line references when sensitive values are encountered.

Risk: The workflow can proceed to GitHub Issue creation and orchestrator execution after approval.

Mitigation: Review Draft SPECs and approval prompts carefully before authorizing issue creation or orchestrated execution.

Risk: Untrusted issue, pull request, comment, or external document text may contain instructions aimed at the agent.

Mitigation: Treat external text as data, quote any embedded directives instead of following them, and require explicit approval before fetching untrusted URLs.

## Reference(s):

- [Gap record reference](references/gap-record.md)
- [Report template reference](references/report-template.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/gap-analysis)
- [Metadata source URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown audit records, Draft SPEC summaries, GitHub issue plans, shell command snippets, and concise Portuguese approval prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analysis by default, with external actions gated by explicit user approval.]

## Skill Version(s):

1.0.1 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
