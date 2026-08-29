## Description:

Detect Task reviews AI-generated ecommerce images before listing and returns a risk level, eight itemized checks, launch guidance, and prompt fixes for reruns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, marketers, and developers use this skill to inspect generated product images before publication. It produces a structured quality report that identifies realism, anatomy, text, lighting, edge, and platform-compliance issues and suggests prompt fixes for reruns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts may be sent to cloud providers for model processing.

Mitigation: Use approved images and prompts only, and confirm that the selected provider is acceptable for the data being inspected.

Risk: Bundled tooling may use local dLazy credentials or third-party provider API keys.

Mitigation: Configure credentials intentionally, rotate or revoke keys when no longer needed, and avoid enabling non-dLazy providers unless required.

Risk: Scripts can write output files and the automated loop can generate or rerun assets.

Mitigation: Prefer direct dLazy inspection commands for routine use, review output paths before execution, and avoid run_loop.mjs unless automatic reruns are intended.

Risk: The model-based report can produce false positives or miss image defects and is not a final legal or platform-policy decision.

Mitigation: Use the report as pre-publication triage and keep human review for final approval, especially for compliance-sensitive listings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/detect-task)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Model flags](artifact/references/model-flags.md)
- [Platform image specifications](artifact/references/platform-specs.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with tables and short English prompt-fix sentences; optional JSON when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single or batch image inputs; reports cover eight fixed risk checks and may include rerun guidance.]

## Skill Version(s):

1.0.1 (source: artifact/SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
