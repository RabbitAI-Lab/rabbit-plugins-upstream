## Description:

Reviews AI-generated e-commerce images before publication, reporting visual risks, eight itemized checks, a publication recommendation, and corrective prompt suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creative teams and listing operators use this skill to assess AI-generated product images for visual defects and potential platform issues before publishing, then decide whether to publish, edit, or regenerate them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to dLazy or another configured provider.

Mitigation: Share only approved images and prompts, and restrict the provider and credentials available to the agent.

Risk: Bundled generation, file-editing, and automatic retry tools extend beyond image inspection and may create derivative files.

Mitigation: Start with a dry run; avoid automated reruns and image fixes unless you explicitly want new or modified files.

Risk: Automated visual review can miss defects or misjudge listing suitability.

Mitigation: Have a person review the image and applicable platform requirements before publication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/detect-task)
- [Model flags](artifact/references/model-flags.md)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report; optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk level, eight itemized findings, publication recommendation, and English corrective prompt sentences.]

## Skill Version(s):

1.0.23 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
