## Description: <br>
Guides an agent through sending local documents such as Word, Excel, PDF, and image files to Feishu users or groups using Feishu Docs, Drive uploads, shared links, and fallback troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business users can use this skill to choose the right Feishu document delivery path, upload generated local files to Feishu Drive, send document links to users or groups, and handle common permission or attachment limitations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to upload local documents to Feishu cloud storage and send links to a user or group. <br>
Mitigation: Confirm the exact file, destination, and recipient before upload or send actions. <br>
Risk: Broad trigger wording could cause the workflow to run for ambiguous requests to send a document through Feishu. <br>
Mitigation: Ask for confirmation when the intended file, recipient, or delivery path is unclear. <br>
Risk: Feishu IM file attachment delivery is documented as unavailable with the current toolchain. <br>
Mitigation: Use the documented fallback of Feishu Docs or Drive links unless an IM file upload tool is available and authorized. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/woai36d/skills/send-doc-to-feishu) <br>
- [Publisher Profile](https://clawhub.ai/user/woai36d) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline command and message templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Feishu document URLs, Drive file links, recipient identifiers, and troubleshooting steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
