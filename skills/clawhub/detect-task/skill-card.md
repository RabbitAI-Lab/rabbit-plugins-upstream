## Description:

Detect Task reviews AI-generated ecommerce images before launch and returns a risk level, eight item-by-item findings, a launch recommendation, and prompt-ready correction phrases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and developers use this skill to screen AI-generated product images before publishing, identify visual defects or platform issues, and feed concise correction phrases back into generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image inputs and credentials may be sent to dLazy or another configured model provider.

Mitigation: Use only images appropriate for the selected provider, verify provider selection before execution, and keep provider credentials scoped and rotated.

Risk: A configurable provider endpoint can send requests outside the expected service boundary.

Mitigation: Set custom provider endpoints only to trusted HTTPS endpoints that the operator controls.

Risk: Generation, fix, and rerun utilities can mutate local outputs and consume credits.

Mitigation: Review commands, use dry runs for planning, constrain output paths and rerun limits, and keep human review in the final publishing workflow.

Risk: Model-based quality checks can miss defects or flag acceptable images incorrectly.

Mitigation: Use the report as a screening aid and retain human final review for launch, legal, and platform policy decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/detect-task)
- [Provider CLI reference](references/provider-cli.md)
- [claude-sonnet-5 model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [Example quality report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown quality report with a risk level, eight findings, a recommendation, and prompt-ready correction phrases; optional scripts may emit JSON manifests.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single-image checks, small image batches, dry-run planning, and optional rerun loops with human review before publishing.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
