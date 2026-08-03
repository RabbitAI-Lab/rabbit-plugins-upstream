## Description: <br>
Feishu App Bot enables agents to read, create, update, and delete Feishu App Bot data through OOMOL's oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent work with connected Feishu App Bot resources, including messages, chats, Drive, Docs, Wiki, Sheets, Slides, Base, Tasks, Calendar, Mail, OKRs, whiteboards, and video meetings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or remove Feishu data when write or destructive actions are approved. <br>
Mitigation: Confirm the exact payload, target resource, and expected effect before running write or destructive actions. <br>
Risk: Feishu business content may pass through the OOMOL connector and transit storage for download-style actions. <br>
Mitigation: Install and use the skill only for connected Feishu App Bot workflows where that data path is acceptable. <br>
Risk: Incorrect action inputs can cause unintended connector behavior. <br>
Mitigation: Inspect the live action schema with the oo CLI before constructing payloads. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-feishu-app-bot) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>
- [Feishu App Bot homepage](https://open.feishu.cn) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent actions are executed through the oo CLI and may return JSON responses from the connector.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
