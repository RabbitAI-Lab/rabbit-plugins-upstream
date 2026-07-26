## Description: <br>
Transfers ownership of Feishu documents, sheets, bitables, and files to a specified user through Feishu Drive permissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[freedompixels](https://clawhub.ai/user/freedompixels) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workspace administrators use this skill to transfer ownership of Feishu business documents to approved users. It is intended for authorized tenant-level document administration where the caller has validated the document token, recipient identity, and approval context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can transfer control of Feishu business documents when run with a tenant token. <br>
Mitigation: Install and run it only when authorized for the tenant, and manually verify the file token, recipient ID, member type, and business approval before execution. <br>
Risk: Tenant tokens are sensitive credentials that can be exposed through shell history, terminal output, or shared logs. <br>
Mitigation: Use secure secret handling and avoid placing real tenant tokens in shell history, examples, or shared logs. <br>
Risk: The security evidence notes too little built-in confirmation or scoping for an ownership-transfer action. <br>
Mitigation: Require operator review before each transfer and prefer least-privileged Feishu application permissions appropriate for the approved task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/freedompixels/skills/feishu-doc-transfer) <br>
- [Publisher profile](https://clawhub.ai/user/freedompixels) <br>
- [Feishu Open Platform](https://open.feishu.cn/app) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, json, guidance] <br>
**Output Format:** [Markdown instructions with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Feishu tenant token, document token, recipient owner ID, member type, and optional document type.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
