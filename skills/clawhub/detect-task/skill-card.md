## Description:

Checks AI-generated ecommerce images before launch, returning a risk level, eight item-by-item judgments, launch guidance, and prompt-ready fix sentences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce creative teams and agents use this skill to inspect AI-generated product or campaign images before publishing. The report helps decide whether to launch, retouch, or rerun generation with targeted prompt fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled workflow includes provider routing, generation/editing, file writing, and rerun behavior beyond a simple read-only image inspection.

Mitigation: Review commands before execution, use dry-run first, pin the provider explicitly, and invoke writing or rerun scripts only when those side effects are intended.

Risk: Provider credentials could be used unintentionally if unrelated API keys are available in the environment.

Mitigation: Avoid exposing unrelated API keys and set the intended provider explicitly before running bundled scripts.

Risk: Model-based quality checks can miss defects, falsely flag acceptable images, or misjudge platform compliance.

Mitigation: Use the report as screening guidance and keep human review for final launch, legal, and platform-rule decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/detect-task)
- [model-flags.md](references/model-flags.md)
- [platform-specs.md](references/platform-specs.md)
- [provider-cli.md](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with structured checklist sections and prompt-fix text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include a risk level, eight fixed risk checks, a launch recommendation, and one to three English prompt-fix sentences when remediation is needed.]

## Skill Version(s):

1.0.14 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
