## Description: <br>
Provides real-time trending news and hot-topic results from Chinese platforms through Xiaobenyang API-backed tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill to fetch and summarize current hot-topic lists from sources such as Weibo, Baidu, Zhihu, Toutiao, Douyin, Bilibili, and other Chinese news or social platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Xiaobenyang API key and stores it in a local plaintext .env file. <br>
Mitigation: Use a limited-scope key if possible, keep unrelated secrets out of the same .env file, and remove or rotate the key after use. <br>
Risk: The shipped tools.py contains a syntax error, so the skill may not run correctly without fixes. <br>
Mitigation: Review and test the installed skill before relying on it for current news results. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/alinklab/skills/real-time-news) <br>
- [Xiaobenyang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text summarizing raw JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Xiaobenyang API key before news tools can return results.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
