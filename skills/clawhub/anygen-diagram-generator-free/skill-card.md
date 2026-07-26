## Description: <br>
Generates basic flowcharts, architecture diagrams, sequence diagrams, and related visuals from text prompts by using the AnyGen CLI and the www.anygen.io server-side rendering service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, product teams, and operations teams use this skill to turn process descriptions and system architecture notes into basic diagrams for documentation, review, and planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Diagram prompts, architecture descriptions, and workflow details are sent to www.anygen.io for rendering. <br>
Mitigation: Do not submit secrets, credentials, confidential architecture details, or sensitive business workflows unless the service and its data handling are approved. <br>
Risk: The skill uses AnyGen CLI authentication and may require users to configure API keys. <br>
Mitigation: Use scoped credentials where possible, keep API keys out of prompts and version control, and rotate keys if exposure is suspected. <br>
Risk: Generated diagrams may be inaccurate or incomplete when prompts are vague or complex. <br>
Mitigation: Review generated diagrams before using them in documentation, and split complex systems into smaller diagram requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/anygen-diagram-generator-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and references to generated diagram image results or structured JSON responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AnyGen CLI authentication and network access to www.anygen.io; generated diagrams should be reviewed before use.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
