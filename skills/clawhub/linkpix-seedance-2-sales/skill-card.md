## Description:

Guides ecommerce and creative teams through generating product-promotion videos with Seedance 2.0 via Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, advertising creatives, and livestream teams use this skill to turn product imagery and selling points into short promotional videos for shopping and social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation or upgrades of unpinned qhkit and related tools may change the local environment.

Mitigation: Review proposed npm, npx, pip, and Node installations before approval; verify the package and version.

Risk: API keys requested in chat or saved in persistent CLI configuration could be exposed.

Mitigation: Provide the token through a secure environment variable or secret store rather than pasting it into chat.

Risk: Selected product images or other media are uploaded to Qinghu AI for processing.

Mitigation: Confirm the selected media is approved for external upload before submitting the task.

Risk: Generating a video spends credits and submitted tasks cannot be canceled.

Mitigation: Review the model, media, duration, and available cost estimate, then obtain explicit approval before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-seedance-2-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video URLs]

**Output Format:** [Text with command examples, task status, and links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos include audio; tasks consume credits and may take up to 40 minutes.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
