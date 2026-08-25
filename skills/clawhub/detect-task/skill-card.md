## Description:

This skill checks AI-generated ecommerce images before launch, reporting quality and compliance risks, launch guidance, and prompt-fix suggestions for regeneration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce, marketing, and creative-operations teams use this skill to screen AI-generated product images before publication. It helps identify visible defects, platform-compliance concerns, and concrete prompt changes for retrying failed images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, prompts, and parameters selected by the user are sent to dLazy's hosted service for analysis.

Mitigation: Confirm hosted processing is acceptable before use and avoid submitting images or prompts that violate internal data-handling rules.

Risk: The workflow depends on the dLazy CLI and a pinned npm package.

Mitigation: Review the pinned CLI package through the organization's supply-chain approval process before installation.

Risk: The skill requires an organization API key for dLazy access.

Mitigation: Use revocable organization API keys and rotate or revoke them from the dLazy dashboard when access changes.

Risk: Model-based image checks can miss defects or flag acceptable images incorrectly.

Mitigation: Use the report as a pre-publication aid and keep human review for final launch decisions, especially for platform-compliance calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/detect-task)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [Example report](https://github.com/dlazyai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown report with risk tables, launch recommendation, and English prompt-fix sentences]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports classify image risk as low, medium, or high and enumerate eight review items with evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
