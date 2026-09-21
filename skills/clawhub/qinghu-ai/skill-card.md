## Description:

青虎AI helps an agent create and transform e-commerce images, videos, ad materials, product-detail assets, POD print designs, storyboards, translated media, and short-video analysis outputs through the qhkit command-line workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content operators use this skill to produce commercial e-commerce media assets, route media requests to the appropriate qhkit command, estimate paid generation tasks, and return generated images, videos, scripts, data files, or text outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires local qhkit setup and may install or update npm packages.

Mitigation: Install it only in environments where agent-managed npm package installation is acceptable, and review package installation before use in sensitive systems.

Risk: The skill stores or uses a Qinghu API token for authenticated media generation.

Mitigation: Use platform secret management or environment variables for the token instead of pasting credentials into chat, and rotate the token if it is exposed.

Risk: The skill uploads local images, videos, and audio files to Qinghu services for estimates or generation tasks.

Mitigation: Submit only media that the user is allowed to upload to Qinghu, and avoid sensitive or confidential files unless the deployment policy permits that transfer.

Risk: Watermark removal, subtitle removal, face replacement, replication, and similar editing features can affect rights-sensitive or identity-sensitive content.

Mitigation: Use those features only for content the user owns or has permission to modify, and confirm rights-sensitive requests before generation.

Risk: Generation actions can consume paid credits and may create tasks that cannot be cancelled after submission.

Mitigation: Run supported estimate actions first, report the expected credit cost and key parameters, and wait for explicit user confirmation before submitting paid generation tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ai)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON parameter examples; generated task results may include media URLs, text, scripts, data files, or status JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a Qinghu API token, model or template selection from live options, estimate before paid submissions where supported, and explicit user confirmation before generation actions.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
