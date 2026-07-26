## Description: <br>
Helps agents draft WeChat Official Account articles, prepare WeChat-compatible HTML and images, and save the result to the account draft box. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mebusw](https://clawhub.ai/user/mebusw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, marketers, and developers use this skill to turn article ideas or markdown drafts into WeChat Official Account drafts with separated titles, uploaded cover art, inserted content images, and practical troubleshooting for common WeChat draft errors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help prepare or upload WeChat Official Account drafts using account credentials. <br>
Mitigation: Keep API keys and browser profiles scoped to the intended account, review generated drafts before submission, and require explicit confirmation before any draft-upload or publish-adjacent step. <br>
Risk: Incorrect title or HTML handling can create duplicate titles, rejected images, malformed JSON, or invalid draft media IDs. <br>
Mitigation: Follow the documented title separation, WeChat image upload, HTML escaping, whitelist, and media ID refresh checks before saving a draft. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mebusw/skills/wechat-mp-draft) <br>
- [Server-resolved GitHub provenance](https://github.com/mebusw/wechat-mp-draft) <br>
- [WeChat permanent media upload endpoint](https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=TOKEN&type=image) <br>
- [WeChat draft batchget endpoint](https://api.weixin.qq.com/cgi-bin/draft/batchget?access_token=$TOKEN) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell command examples, JSON examples, and HTML handling instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces draft-preparation guidance and command sequences; generated drafts should be reviewed before submission or publishing.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
