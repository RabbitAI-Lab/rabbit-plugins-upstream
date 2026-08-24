## Description:

Uploads product assets and guides an agent through LinkPix/qhkit commands to generate short e-commerce sales videos with AI scripts, voiceover, captions, and transitions for platforms such as TikTok and Douyin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, sellers, and agents use this skill to prepare and submit LinkPix/qhkit video-generation jobs from product images, selling points, reference media, and language or orientation choices. It is intended for e-commerce short-video workflows, including quote checks, job submission, status polling, and final video delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask users to provide API keys for qhkit configuration.

Mitigation: Use platform-managed secrets or temporary scoped tokens where possible, and avoid pasting long-lived API keys into chat.

Risk: The setup flow may run global npm, curl, pip, or npx installation commands.

Mitigation: Review installation commands before use and run them only in an environment where those runtime changes are acceptable.

Risk: Video-generation submissions can consume credits and may not be cancellable after task creation.

Mitigation: Confirm model, duration, assets, language, orientation, and estimated credits before running any generate command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-sales-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, status summaries, credit estimates, and generated video URLs when the external service returns them.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
