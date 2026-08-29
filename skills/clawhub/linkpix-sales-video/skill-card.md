## Description:

Uploads product materials to generate sales short videos with AI scripts, voiceover, subtitles, and transitions for platforms such as TikTok and Douyin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, creators, and agents use this skill to prepare LinkPix/qhkit workflows for product sales videos, including model discovery, cost estimates, task submission, status polling, and video delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may expose a production qhkit API key if the user pastes it into chat.

Mitigation: Use a local environment variable, secret manager, or direct terminal entry for the token, and rotate the key if it is exposed.

Risk: Product images, reference videos, or audio are uploaded to LinkPix/qhkit services and generation can spend account credits.

Mitigation: Install and run only when the user accepts that upload and credit-spend behavior, and require explicit confirmation before generation commands that consume credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-sales-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline bash commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return qhkit task IDs, status JSON, generated video URLs, and credit estimates.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
