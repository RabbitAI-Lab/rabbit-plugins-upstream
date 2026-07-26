## Description: <br>
一个用于从Bilibili视频URL中检索字幕、弹幕和评论信息的MCP服务器。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve and summarize Bilibili video subtitles, danmaku, and popular comments from a provided video URL through the XiaoBenYang API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persists a user API key in plaintext. <br>
Mitigation: Use a narrowly scoped or disposable API key, avoid sharing the key in chat, and confirm that `.env` is not committed or synced. <br>
Risk: Documentation drift may confuse users about the package purpose or expected behavior. <br>
Mitigation: Review the skill instructions and package contents before broad deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/bilibili-video-info) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or structured text summarizing JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Bilibili video URL and a configured XBY_APIKEY.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
