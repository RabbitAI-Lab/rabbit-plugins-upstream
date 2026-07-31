## Description: <br>
将用户已授权账号中的抖音视频收藏或用户明确指定的喜欢列表配置并同步到本地 Markdown 或 Obsidian 知识库；默认收藏，只有用户明确说喜欢/点赞才切换来源。首次明确选择推荐的百炼转录、本地 Whisper 或不转录。不得绕过登录、访问他人账号或泄露 Cookie 与私密数据。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tars1230](https://clawhub.ai/user/tars1230) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and operate syncing of their own authorized Douyin favorites, or explicitly selected liked videos, into a local Markdown or Obsidian knowledge base with optional transcription. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles a user's own Douyin favorites or liked-video data and may sync private viewing metadata into a local knowledge base. <br>
Mitigation: Use only an account the user has authorized, keep favorites and liked-video outputs isolated, and confirm the target knowledge-base directory before setup or sync. <br>
Risk: Bailian transcription requires DASHSCOPE_API_KEY and may incur cloud transcription costs. <br>
Mitigation: Store DASHSCOPE_API_KEY only in an environment variable, keychain, or secret manager, and review current Bailian pricing before enabling cloud transcription. <br>
Risk: Login, cookies, browser profiles, and local paths can expose private account or machine details if mishandled. <br>
Mitigation: Do not request, print, store, or pass cookies or browser profile data; let the user complete login in their own terminal and avoid exposing credentials in config, notes, or logs. <br>
Risk: The referenced repository is third-party software outside NVIDIA ownership. <br>
Mitigation: Confirm trust in the referenced douyin-favorites-to-knowledge repository before installation or scheduled execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tars1230/skills/douyin-favorites-to-knowledge) <br>
- [Gitee repository referenced by the skill](https://gitee.com/tars123/douyin-favorites-to-knowledge.git) <br>
- [GitHub repository referenced by the skill](https://github.com/tars1230/douyin-favorites-to-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup, sync, troubleshooting, scheduling, and verification guidance for an agent; it does not directly expose credentials or cookies.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
