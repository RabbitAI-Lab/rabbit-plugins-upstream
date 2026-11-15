## Description:

Summarizes CodexBar local cost usage by model for Codex or Claude, including current-model and all-model cost breakdowns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect local CodexBar cost data and summarize which Codex or Claude models drove usage costs. It supports quick current-model reporting, full per-model breakdowns, provider selection, file/stdin input, and text or JSON output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill summarizes local CodexBar cost data derived from Codex or Claude session logs.

Mitigation: Install only where local usage-cost reporting is acceptable, and avoid sharing generated reports when model names, dates, or costs are sensitive.

Risk: The skill depends on the external CodexBar CLI/Homebrew cask to collect the underlying usage data.

Mitigation: Review and trust the CodexBar CLI and its Homebrew cask separately before using the skill.

## Reference(s):

- [CodexBar CLI quick ref](references/codexbar-cli.md)
- [ClawHub Model Usage skill page](https://clawhub.ai/eohmig/skills/model-usage)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON, with Markdown documentation examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cost-only per-model summaries; CodexBar output does not split tokens by model.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
