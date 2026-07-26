## Description: <br>
AI Notes of Video helps agents create and query Baidu AI note-generation tasks for user-provided video URLs, returning document, outline, and image-text notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baiduqianfangroup](https://clawhub.ai/user/baiduqianfangroup) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to submit a video URL to Baidu Qianfan, poll the resulting task, and retrieve generated document, outline, or image-text notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Baidu API key that could be exposed through shared logs, shell history, or reused credentials. <br>
Mitigation: Use a scoped Baidu API key where possible and avoid printing or storing the key in shared logs, command history, or examples. <br>
Risk: User-provided video URLs are submitted to Baidu's service, which may be inappropriate for private, internal, signed, authenticated, or sensitive videos. <br>
Mitigation: Submit only video URLs that the user is authorized to share with Baidu and avoid private or sensitive URLs unless sharing is approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/baiduqianfangroup/skills/ai-notes-of-video) <br>
- [Publisher profile](https://clawhub.ai/user/baiduqianfangroup) <br>
- [Baidu Qianfan AI note task creation API](https://qianfan.baidubce.com/v2/tools/ai_note/task_create) <br>
- [Baidu Qianfan AI note task query API](https://qianfan.baidubce.com/v2/tools/ai_note/query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [JSON responses from helper scripts plus Markdown guidance with shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, the requests package, BAIDU_API_KEY, a video URL for task creation, and a task ID for polling.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
