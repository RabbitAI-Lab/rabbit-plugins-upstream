## Description:

Reviews pre-publication AI-generated ecommerce images and returns a risk level, eight checklist judgments, an advertising recommendation, and prompt-ready fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and agents use this skill to inspect AI-generated product or advertising images before publication. It helps decide whether to publish, retouch, or regenerate an image and supplies concise correction text for the next generation pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images may be routed to an external cloud provider, which can expose sensitive product or campaign imagery.

Mitigation: Use only approved provider credentials and avoid submitting sensitive images unless cloud processing is acceptable.

Risk: The bundled unified generator can select providers and save generated or modified files beyond a read-only checking workflow.

Mitigation: Prefer the direct dLazy text-model command or force an approved provider when a read-only review path is required.

Risk: The visual assessment can produce false positives or miss defects and does not replace platform, legal, or human review.

Mitigation: Treat reports as advisory, review the evidence for each flagged item, and keep human approval before publishing.

## Reference(s):

- [Skill page](https://clawhub.ai/dlazyai/skills/detect-task)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [Example report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Structured Markdown report with command examples and prompt-ready correction text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include a risk level, eight fixed risk checks, publication guidance, and one to three English correction phrases when revision is recommended.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
