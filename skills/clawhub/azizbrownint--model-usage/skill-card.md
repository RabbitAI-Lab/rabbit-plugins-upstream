## Description:

Summarize CodexBar local cost logs by model for Codex or Claude, including current or full breakdowns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to summarize local CodexBar cost logs by model for Codex or Claude, either for the current model or for all model breakdowns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live mode depends on CodexBar reading local Codex or Claude usage logs.

Mitigation: Use live mode only when local log access is acceptable, or run the script with an exported JSON file via --input.

Risk: Live mode depends on a third-party CodexBar Homebrew package.

Mitigation: Review the CodexBar package and installation source before installing it.

## Reference(s):

- [CodexBar CLI quick ref](references/codexbar-cli.md)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/model-usage)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples; script output is plain text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cost-only per-model summaries; token counts are not split by model in CodexBar output.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
