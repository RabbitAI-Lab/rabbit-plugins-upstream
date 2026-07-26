## Description: <br>
WeChat Official Account draft management toolkit for listing, creating, updating, and deleting drafts, uploading materials, generating cover images, and preparing article digests through official WeChat APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andy8663](https://clawhub.ai/user/andy8663) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use the skill to manage WeChat Official Account draft and material workflows from an agent, including draft creation, updates, deletion, cover generation, and relay or direct API publishing setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose long-lived WeChat Official Account AppSecret values, draft content, media, and account actions to a relay operator. <br>
Mitigation: Install only if the publisher and relay operator are trusted; prefer direct mode where possible, use HTTPS-only relay endpoints, rotate credentials after testing, and protect config and cache files. <br>
Risk: Draft or material deletion and publish-adjacent actions may run without enough built-in safeguards. <br>
Mitigation: Require manual confirmation before an agent performs delete or publish-related actions, and limit the configured account credentials to the minimum needed scope. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/andy8663/skills/wechat-oa) <br>
- [WeChat Official Platform](https://mp.weixin.qq.com) <br>
- [WeChat Official Account API reference](artifact/references/wechat_api.md) <br>
- [Relay service product page](https://saas.synergyinfo.tech/products/wechat-oa) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text with CLI commands, JSON configuration snippets, and generated article assets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update WeChat drafts, upload media, generate cover images, cache access tokens, and write local cache files when configured.] <br>

## Skill Version(s): <br>
3.0.3 (source: server release, SKILL.md frontmatter, pyproject.toml, skill.json; changelog top entry is 3.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
