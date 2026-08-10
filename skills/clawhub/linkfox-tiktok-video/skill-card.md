## Description:

A LinkFox TikTok creator video API skill that helps agents call shoppable-video, creator-profile, product-selection, precheck, publishing, and status endpoints through the TikTok video gateway after authorization is handled by linkfox-tiktok-video-auth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to manage TikTok creator shoppable-video workflows after authorization, including product selection, video precheck, publishing, status checks, and creator or product data retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive TikTok creator data, product data, posting workflow data, or access tokens may be exposed if passed through chat or stored carelessly.

Mitigation: Use the skill only with the intended LinkFox gateway and auth skill, avoid sharing raw tokens in chat, and review requests before execution.

Risk: Automatic feedback reporting may send contextual information outside the immediate workflow.

Mitigation: Disable or avoid feedback reporting unless the user or deploying organization consents to that data flow.

Risk: Large response persistence can leave raw API responses on disk.

Mitigation: Write response_io.py outputs only to temporary private directories and delete them after use.

## Reference(s):

- [TikTok Video API Reference](references/api.md)
- [Shoppable Video Large File Upload Solution](references/large-file-upload.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-video)
- [LinkFox Skill Publisher](https://clawhub.ai/user/linkfox-ai)
- [TikTok Shop Partner Center: Shoppable Video Large File Upload](https://partner.tiktokshop.com/docv2/page/shoppable-video-large-file-upload)
- [LinkFox Gateway](https://tool-gateway.linkfox.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with inline shell commands and JSON API parameters or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist large API responses to temporary local files when response_io.py is used.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
