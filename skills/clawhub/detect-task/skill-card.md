## Description:

Reviews AI-generated product images before publication and provides a risk assessment, eight-item checklist, publication recommendation, and prompt corrections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and content reviewers assess AI-generated product images before publication, identify visual defects, and prepare corrections for another review cycle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image and prompt content may be sent to dLazy or another configured model provider.

Mitigation: Select the provider explicitly and review image and prompt sensitivity before submission.

Risk: Bundled generation, file-writing, and automatic retry or fix options extend beyond image checking.

Mitigation: Use only the checking workflow unless generation or file changes are intended; review output paths and proposed corrections before enabling those options.

Risk: Image judgments can miss defects or incorrectly flag acceptable images.

Mitigation: Have a person review the findings and the final image before publication.

## Reference(s):

- [ClawHub detect-task listing](https://clawhub.ai/dlazyai/skills/detect-task)
- [Provider CLI reference](references/provider-cli.md)
- [Platform specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report; optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk level, eight findings with evidence, publication recommendation, and optional English prompt corrections.]

## Skill Version(s):

1.0.25 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
