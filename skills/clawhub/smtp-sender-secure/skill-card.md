## Description: <br>
Send emails through MGC Blackbox by storing SMTP credentials and mail scripts locally, then executing the stored script with MGC tools so the agent receives only execution results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zkeviny](https://clawhub.ai/user/zkeviny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to document and configure MGC Blackbox workflows for sending SMTP email while keeping credentials out of the agent prompt. It is suited to workflows where users explicitly approve sends and manage credential storage, recipient limits, and audit controls outside the skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is described as documentation-only, but the artifact includes runnable example code that can read local MGC credentials and send SMTP email. <br>
Mitigation: Review the script before use, store credentials only through the intended user-controlled MGC flow, and require explicit approval before every send. <br>
Risk: Zero-exposure claims may be misunderstood as meaning credentials are inaccessible to runtime code. <br>
Mitigation: Treat credentials as accessible to the local script at execution time, and enforce recipient allowlists, send limits, logging, and audit controls outside the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/smtp-sender-secure) <br>
- [Publisher profile](https://clawhub.ai/user/zkeviny) <br>
- [MGC Blackbox repository](https://github.com/zkeviny/MGC-Blackbox) <br>
- [MGC Blackbox issues](https://github.com/zkeviny/MGC-Blackbox/issues) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces documentation and example script patterns for MGC-based SMTP sending; users supply credentials, recipients, subjects, and message bodies.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release evidence, artifact frontmatter, and manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
