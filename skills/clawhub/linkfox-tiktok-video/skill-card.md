## Description:

This skill helps agents use LinkFox's TikTok Video developer proxy to retrieve creator profile and product data, precheck shoppable videos, publish shoppable videos, and check posting status after creator authorization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide authenticated TikTok creator video workflows through LinkFox, including product selection, content precheck, shoppable video posting, and status checks. It is not an authorization skill and depends on linkfox-tiktok-video-auth for creator tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox and TikTok creator tokens for user-directed creator operations, including public posting.

Mitigation: Install only when that access is acceptable, avoid passing raw tokens on the command line where possible, and verify the selected creator account and post parameters before execution.

Risk: Persisted API response files may contain sensitive creator, product, token, or posting data.

Mitigation: Write response dumps outside shared or synced directories, keep them out of version control, and delete them after extracting the needed fields.

Risk: Automatic Feedback API submission could send operational context outside the user's immediate workflow.

Mitigation: Disable feedback submission or require explicit approval before sending feedback.

Risk: Several documented binary upload and large-file paths are not currently callable through the LinkFox developer proxy.

Mitigation: Use the skill's documented proxy-supported endpoints only, and treat large-file upload init, bind, and direct chunk upload as manual or externally supported steps until the proxy supports them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-video)
- [TikTok video API reference](references/api.md)
- [Shoppable Video Large File Upload Solution](references/large-file-upload.md)
- [Shoppable video Integration Solutions V2025.Q4.01](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f)
- [TikTok Shop Partner Center large file upload](https://partner.tiktokshop.com/docv2/page/shoppable-video-large-file-upload)
- [Get Creator Profile 202508](https://partner.tiktokshop.com/docv2/page/get-creator-profile-202508)
- [Get Shop Products 202509](https://partner.tiktokshop.com/docv2/page/get-shop-products-202509)
- [Get Showcase Products 202405](https://partner.tiktokshop.com/docv2/page/get-showcase-products-202405)
- [Upload Shoppable Video File 202505](https://partner.tiktokshop.com/docv2/page/upload-shoppable-video-file-202505)
- [Post Shoppable Video 202607](https://partner.tiktokshop.com/docv2/page/post-shoppable-video-202607)
- [Get Shoppable Video Status 202509](https://partner.tiktokshop.com/docv2/page/get-shoppable-video-status-202509)
- [Pre-check Shoppable Video 202511](https://partner.tiktokshop.com/docv2/page/precheck-shoppable-video-202511)
- [Get Shoppable Video Pre-check Result 202511](https://partner.tiktokshop.com/docv2/page/get-shoppable-video-precheck-result-202511)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist large API responses to local files for later field extraction.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
