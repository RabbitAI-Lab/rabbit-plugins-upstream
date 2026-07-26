## Description: <br>
Fetches a real-time whole-network hot-search list that aggregates trending topics from Weibo, Douyin, Baidu, NetEase, and other platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to fetch and summarize current cross-platform trending topics from TianAPI using a configured API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The TianAPI API key could be exposed if it is placed directly in commands, URLs, screenshots, logs, or shared terminal history. <br>
Mitigation: Set TIANAPI_NETWORK_HOT_KEY as an environment variable or store it in a restricted local secret file, and avoid sharing command lines or output that contain the key. <br>


## Reference(s): <br>
- [TianAPI Network Hot API](https://www.tianapi.com/apiview/223) <br>
- [TianAPI Network Hot endpoint](https://apis.tianapi.com/networkhot/index) <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-network-hot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text summaries, with optional JSON returned from the TianAPI request.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and TIANAPI_NETWORK_HOT_KEY; API result items include title, digest, and hotnum fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
