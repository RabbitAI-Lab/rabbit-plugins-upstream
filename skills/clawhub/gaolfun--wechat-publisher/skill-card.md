## Description: <br>
自动将 Markdown 文章转换成微信公众号支持的 HTML，上传图片并发布到草稿箱或直接群发文章。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gaolfun](https://clawhub.ai/user/gaolfun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
内容创作者和运营人员可让 agent 将 Markdown 文章转换为微信公众号兼容的 HTML，上传封面和正文图片，创建草稿，并在确认后提交发布。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles WeChat Official Account credentials and local token files. <br>
Mitigation: Install it only when the agent should use those credentials, keep AppSecret and token files private, and restrict their file permissions. <br>
Risk: The skill can upload article content and images to WeChat and may submit content for publication. <br>
Mitigation: Confirm every upload or direct publication, and avoid using confidential drafts unless sending that content and its images to WeChat is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gaolfun/skills/wechat-publisher) <br>
- [WeChat Official Accounts Platform](https://mp.weixin.qq.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, HTML, API Calls, Configuration, Guidance] <br>
**Output Format:** [Markdown response with status summaries, HTML snippets, JSON API payloads, image URL mappings, and WeChat media or publish IDs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include access_token status, uploaded image URLs, thumb_media_id, draft media_id, publish_id, and error-code guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
