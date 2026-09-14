## Description:

This skill guides agents through using Qinghu qhkit to analyze a shared short-form video, rewrite its structure for a user's product, and submit a Seedance 2.5 video-generation job after explicit confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, MCN teams, brand marketers, and ecommerce sellers use this skill to adapt the emotional pacing, shot structure, and visual style of a viral short video into product-specific video creative for channels such as Douyin, TikTok, Xiaohongshu, Kuaishou, and WeChat Channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt for a Qinghu API key in chat.

Mitigation: Configure the token locally through an environment variable or secure secret mechanism, do not paste it into chat, and rotate the key if it was shared.

Risk: The skill can install or upgrade qhkit and helper packages through mutable package-manager commands.

Mitigation: Review the package source and install commands before execution, use a controlled environment, and avoid granting unnecessary privileges.

Risk: The workflow processes local media, uploads media to Qinghu, and can submit paid video-generation jobs.

Mitigation: Proceed only after confirming the selected media, model, duration, and estimated credits with the user, and ensure the user has rights to the input media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedance-25-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce rewritten video scripts, task IDs, status summaries, credit estimates, and video result URLs when the agent executes qhkit commands.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
