## Description:

Reviews AI-generated ecommerce images before launch and returns a risk level, eight quality checks, a launch recommendation, and prompt-ready fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and developers use this skill to QA AI-generated product images before paid placement or storefront publication. It helps triage whether an image can launch, should be rerun, or needs manual editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inspection inputs may be routed to dLazy or another configured provider, including uploading local images and prompts.

Mitigation: Use --dry-run before execution, choose the provider explicitly, and avoid sensitive assets unless the selected provider's data handling is acceptable.

Risk: The wrapper can route through generic image generation or editing providers despite the skill's analysis-only intent.

Mitigation: Prefer the direct dlazy claude-sonnet-5 path for QA, or explicitly pin a text-capable provider and verify the result is read from result.data.texts[0].

Risk: Model-based image QA can miss defects or flag acceptable images incorrectly.

Mitigation: Use the report for triage, review the evidence for each hit, and keep human final review before publication or platform compliance decisions.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [claude-sonnet-5 Model Flags](references/model-flags.md)
- [Platform Image Specifications](references/platform-specs.md)
- [Detect Task Example Report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown QA report with optional shell commands and prompt-fix text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include a risk level, eight pass/hit findings with evidence, a launch recommendation, and one to three English prompt-fix sentences when remediation is needed.]

## Skill Version(s):

1.0.13 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
