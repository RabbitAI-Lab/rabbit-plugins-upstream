## Description: <br>
Fetches the title and body text of a single Zhihu column article from a zhuanlan.zhihu.com/p/... URL using browser session, cookie file, or simulated-header fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve and save structured content from individual Zhihu column article URLs when normal page fetching returns access errors or incomplete content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use a logged-in Zhihu session or stored Zhihu cookies to fetch articles. <br>
Mitigation: Treat cookies like passwords, restrict access to the cookie file, avoid sharing logs or archives that contain cookies, and rotate or clear cookies after use. <br>
Risk: The skill uses anti-bot bypass techniques and may violate site access rules. <br>
Mitigation: Use it only for content the operator is authorized to access, follow applicable site terms and rate limits, and stop using it if access is denied. <br>
Risk: The security verdict is suspicious because safety guidance around cookies and access behavior is limited. <br>
Mitigation: Review the skill and its configuration before deployment, and require explicit operator approval before running fetch commands against Zhihu. <br>


## Reference(s): <br>
- [Zhihu Article Fetcher on ClawHub](https://clawhub.ai/woai36d/skills/zhihu-article-fetcher) <br>
- [Publisher profile](https://clawhub.ai/user/woai36d) <br>
- [Zhihu](https://www.zhihu.com) <br>
- [Zhihu column article URL pattern](https://zhuanlan.zhihu.com/p/660571164) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration] <br>
**Output Format:** [JSON output with optional saved JSON file, plus Markdown instructions and shell commands for the agent workflow] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes fetch metadata, article title, source URL, extracted text content, word count, and fetch method.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
