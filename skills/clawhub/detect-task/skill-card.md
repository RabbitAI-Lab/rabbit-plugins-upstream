## Description:

This skill reviews pre-launch AI product images and produces a risk level, eight inspection findings, an advertising recommendation, and prompt-ready correction sentences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to inspect AI-generated product images before launch, identify visual defects or platform-readiness issues, and obtain concise prompt fixes for regeneration or manual repair.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to dLazy or configured third-party providers during inspection.

Mitigation: Avoid sensitive images or private image URLs unless provider routing and credentials are explicitly controlled.

Risk: Bundled helper scripts include broader image generation, editing, and rerun workflows beyond the narrow inspection task.

Mitigation: Prefer the direct dLazy claude-sonnet-5 inspection command for this skill, and review or remove generic generation scripts for narrow deployments.

Risk: Model-based image quality findings can include false positives or missed defects and do not replace legal or platform policy review.

Mitigation: Use the report as pre-screening guidance, verify evidence for flagged items, and keep human final review before publishing.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [claude-sonnet-5 Model Flags](references/model-flags.md)
- [Platform Image Specs](references/platform-specs.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/detect-task)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report text with optional shell command examples and prompt correction sentences]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include risk level, eight fixed inspection categories, launch recommendation, and one to three prompt-ready correction sentences when remediation is needed.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
