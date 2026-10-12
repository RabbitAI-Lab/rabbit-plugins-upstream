## Description:

Reviews AI-generated ecommerce images before publication and returns a risk level, eight itemized checks, a publication recommendation, and prompt-ready fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams use this skill to screen AI-generated product images for visible defects and potential listing issues before publication, with suggested corrections for regeneration or manual retouching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts may be sent to third-party services, including generation or editing providers beyond image inspection.

Mitigation: Review before using private or regulated assets; confirm upload destinations and choose the direct dLazy inspection path or an explicit provider instead of automatic selection.

Risk: Automated image checks may miss defects or misjudge marketplace compliance.

Mitigation: Have a person review images and applicable platform rules before publishing.

## Reference(s):

- [Model flags](references/model-flags.md)
- [Platform specifications](references/platform-specs.md)
- [Provider CLI and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown report with a risk rating, eight checks, a publication recommendation, and prompt-ready corrections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can request JSON output; human review remains necessary for final publication and platform compliance.]

## Skill Version(s):

1.0.21 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
