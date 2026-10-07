## Description:

Reviews AI-generated e-commerce images before listing, reporting eight visual and compliance checks, an overall risk level, and prompt-ready corrections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce content teams and developers use this skill to screen AI-generated product images before publication and obtain specific corrections for editing or another generation pass. Human review remains necessary before listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unreleased product images and prompts may be sent to a configured cloud provider.

Mitigation: Use only approved images and an explicitly selected provider; avoid sensitive inputs without authorization.

Risk: Provider calls and automatic reruns may incur costs.

Mitigation: Use dry-run before paid calls and set appropriate limits for repeated runs.

Risk: Bundled helpers can generate or edit media and write derived files, beyond image review.

Mitigation: Review output paths and requested actions before invoking run-loop or --fix modes.

Risk: Image assessments can miss defects or incorrectly clear images for publication.

Mitigation: Require human final review and verify platform requirements before listing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/detect-task)
- [Example image review report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [Provider CLI reference](references/provider-cli.md)
- [Platform image specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with a risk table and prompt-ready correction sentences; optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Helper scripts can save generated or edited media and run records when invoked.]

## Skill Version(s):

1.0.18 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
