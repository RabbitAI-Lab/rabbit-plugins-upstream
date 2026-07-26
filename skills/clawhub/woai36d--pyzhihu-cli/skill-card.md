## Description: <br>
Pyzhihu Cli helps an agent use the pyzhihu-cli Zhihu command-line tool for search, hot lists, questions, answers, comments, feeds, user profiles, posting, deleting the user's own content, voting, following, collections, and notifications while keeping Zhihu cookies local. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Zhihu users can use this skill to have an agent translate natural-language Zhihu tasks into local `zhihu` CLI commands, summarize structured query results, and assist with logged-in account actions when the user approves them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through account-changing Zhihu actions, including posting, voting, following, and deleting the user's own content. <br>
Mitigation: Require explicit user confirmation before posting, voting, following, or deleting content, and confirm exact content IDs before destructive commands. <br>
Risk: Zhihu cookies and QR login artifacts can expose account access if copied into untrusted contexts or left in shared media folders. <br>
Mitigation: Keep cookies local, avoid pasting cookies into untrusted chats or logs, prefer QR login, and remove copied login_qrcode.png files after login completes or times out. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/woai36d/skills/pyzhihu-cli) <br>
- [Publisher profile](https://clawhub.ai/user/woai36d) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and summarized CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses JSON CLI output for supported data queries; account-changing operations depend on local Zhihu authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
