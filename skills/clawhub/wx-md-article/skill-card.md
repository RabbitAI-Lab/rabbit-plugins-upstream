## Description: <br>
Convert a local Markdown article into clean WeChat Official Account HTML, with an optional explicitly confirmed draft upload. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content creators use this skill to turn reviewed Markdown drafts into WeChat-ready HTML and, when explicitly confirmed, upload a draft to a configured WeChat Official Account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Upload mode can send article HTML and an optional cover image to a WeChat Official Account. <br>
Mitigation: Review the generated HTML, cover image, and destination account before running with both --upload and --confirm-upload. <br>
Risk: Upload mode requires WeChat account credentials. <br>
Mitigation: Keep WECHAT_APP_ID, WECHAT_APP_SECRET, and account values in environment variables or a secret store; do not place credentials in skill files, chats, commands, or logs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yangchao228/skills/wx-md-article) <br>
- [Project Homepage](https://github.com/yangchao228/wx-md-article) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; generated artifact is HTML] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default local-only HTML generation; network upload requires --upload and --confirm-upload.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
