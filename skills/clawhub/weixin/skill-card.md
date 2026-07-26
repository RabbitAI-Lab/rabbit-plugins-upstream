## Description: <br>
Weixin helps agents operate WeChat Official Account and Mini Program APIs with a zero-dependency CLI plus practical guidance for token, media, draft, publishing, OAuth, JSSDK, and payment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent call WeChat Official Account and Mini Program APIs, manage access tokens and media, create drafts, publish articles, inspect publishing records, and troubleshoot common production API errors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles powerful WeChat account credentials and may print access tokens in command output. <br>
Mitigation: Treat WX_SECRET and access_token values as secrets, avoid logging command output, and restrict use to accounts the operator is authorized to manage. <br>
Risk: Publishing, template-message, and generic write calls can affect live user-facing WeChat accounts. <br>
Mitigation: Require explicit user confirmation before publishing content, sending template messages, or using the generic call command for write actions. <br>
Risk: Independent token refreshes can invalidate production access tokens or race with an existing service. <br>
Mitigation: Use a centralized token cache for production accounts and avoid running ad hoc token refreshes against accounts managed by another service. <br>


## Reference(s): <br>
- [ClawHub Weixin Skill](https://clawhub.ai/zhangifonly/skills/weixin) <br>
- [WeChat Official Account API endpoint](https://api.weixin.qq.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses from the bundled CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled CLI reads WX_APPID and WX_SECRET, calls WeChat API endpoints, prints JSON responses, and caches access tokens in the system temporary directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
