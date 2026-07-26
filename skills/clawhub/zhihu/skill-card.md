## Description: <br>
Manage Zhihu AI Bot integration for publishing pins to Zhihu Rings, liking or unliking pins and comments, creating and deleting comments, and fetching ring or comment details using Zhihu API credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[keepwonder](https://clawhub.ai/user/keepwonder) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to let an agent interact with a configured Zhihu account for ring content publishing, reactions, comments, and content lookup. It is intended for workflows where the operator has valid Zhihu API credentials and authorization to act on the target account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish, react, comment, and delete live Zhihu content through a configured account. <br>
Mitigation: Require manual confirmation after reviewing the exact target content, action, and comment or pin ID before executing write or delete commands. <br>
Risk: Zhihu API credentials can authorize account actions if exposed or reused broadly. <br>
Mitigation: Store ZHIHU_APP_KEY and ZHIHU_APP_SECRET outside version control with restricted permissions, and use dedicated credentials when possible. <br>
Risk: Automated interactions may affect public or account-visible content. <br>
Mitigation: Limit use to authorized accounts and intended rings, and review the generated command arguments before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/keepwonder/skills/zhihu) <br>
- [Publisher profile](https://clawhub.ai/user/keepwonder) <br>
- [Zhihu OpenAPI base URL](https://openapi.zhihu.com/) <br>
- [Supported Zhihu Ring](https://www.zhihu.com/ring/host/2001009660925334090) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and command-line text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses ZHIHU_APP_KEY and ZHIHU_APP_SECRET environment variables to sign requests to the Zhihu API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
