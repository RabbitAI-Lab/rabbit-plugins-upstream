## Description:

Reviews AI-generated ecommerce images before publication and returns a risk rating, eight-item findings, a publishing recommendation, and suggested prompt corrections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and image reviewers use this skill to screen generated product imagery for visual defects and potential listing concerns before publication, and to guide manual fixes or regeneration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private product images and prompts may be sent to a cloud provider; bundled helpers can route them to generation or editing services.

Mitigation: Review the data destination before use; prefer the direct dLazy text-model path or a dry run, and avoid unrelated provider credentials in the environment.

Risk: Optional fixing and rerun commands can rewrite files or trigger additional generation requests.

Mitigation: Do not run --fix or run_loop unless file changes and generation reruns are intended; review commands and outputs first.

Risk: Automated image judgments can miss defects or incorrectly flag compliant images.

Mitigation: Keep a human final review and confirm current marketplace requirements before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/detect-task)
- [Example image review report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [Provider CLI reference](references/provider-cli.md)
- [Image listing specifications](references/platform-specs.md)
- [Model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown report with a risk rating, eight-item findings table, recommendation, and optional English prompt corrections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional JSON report; batch workflows may write reports and rerun queues. Results require human review before publication.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
