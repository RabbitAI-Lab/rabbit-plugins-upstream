## Description:

This skill helps agents replace or localize ecommerce product-image and video models through LinkPix/qhkit while preserving clothing, pose, composition, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and agents use this skill to generate localized product imagery or video by replacing a model's face or person through qhkit/LinkPix. It is intended for authorized media and likenesses where users need market-specific model presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images or videos may be sent to the external qhkit/LinkPix service.

Mitigation: Use only media that is authorized for upload and editing, and avoid sensitive or restricted content unless the user has approval.

Risk: Face or person replacement can misuse a real person's likeness.

Mitigation: Confirm authorization for any real-person likeness before processing and refuse unauthorized replacement requests.

Risk: The skill may require a qhkit API key, and sharing keys in chat can expose credentials.

Mitigation: Prefer a local environment variable, credential vault, or other secure secret flow; revoke and rotate any key already shared in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-face-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide media submission to qhkit/LinkPix and return image or video URLs after task completion.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
