## Description:

Launch and drive coding agents (codex, claude, agy) through the Herdr CLI; requires a herdr pane (HERDR_ENV=1). Use before starting or prompting a herdr subagent, and when a herdr command fails or an agent seems stuck or silently lost a prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to launch, monitor, and troubleshoot Herdr-managed coding agents from a Herdr pane. It provides operational guidance, shell command patterns, and configuration notes for Codex, Claude Code, and Antigravity CLI agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes guidance for pre-seeding trust, reducing approval prompts, and running child agents with permissive modes.

Mitigation: Use only in trusted repositories, and avoid pre-trust, auto-approval, accept-edits, or permissive child-agent configuration unless the operator intentionally accepts those reduced prompts.

Risk: Herdr commands can affect the wrong pane when run outside a Herdr-managed pane or when agent state is inferred incorrectly.

Mitigation: Require HERDR_ENV=1 before using the workflow, read the target pane or agent detection output before prompting, and confirm state by visible effect rather than exit code alone.

## Reference(s):

- [Herdr documentation](https://herdr.dev)
- [herdr-faq upstream homepage](https://github.com/tenequm/skills/tree/main/skills/herdr-faq)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational guardrails for running child coding agents through Herdr.]

## Skill Version(s):

0.4.1 (source: frontmatter, changelog, release metadata; released 2026-09-11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
