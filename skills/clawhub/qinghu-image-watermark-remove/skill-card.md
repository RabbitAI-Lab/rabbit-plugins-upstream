## Description:

This skill helps agents use Qinghu AI to remove watermarks, logos, and optional text from a single image while restoring background texture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to process authorized image assets through Qinghu AI when they need watermarks, logos, marks, or optional embedded text removed. It is suited to single-image ecommerce and social media image cleanup workflows where the user confirms cost before job submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are uploaded to Qinghu's service for processing.

Mitigation: Use the skill only when the user is comfortable sending the chosen image to Qinghu and avoid sensitive or unauthorized images.

Risk: The workflow uses a Qinghu API token and may consume Qinghu credits.

Mitigation: Store the token carefully, run an estimate first, present the expected charge, and submit the paid job only after explicit user confirmation.

Risk: Removing watermarks or text from third-party images can create copyright or authorization concerns.

Mitigation: Use the workflow only on images the user owns or is authorized to edit, especially for commercial use.

Risk: Large images may be compressed and the output resolution may differ from the input.

Mitigation: Warn users with strict size requirements before submission and verify the returned image dimensions after completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-watermark-remove)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON parameters; completed runs return image URLs from the Qinghu workflow status response.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes one image per workflow run; image output dimensions may differ from the source image; credits are estimated before submission and finalized after status completes.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
