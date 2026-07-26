## Description: <br>
Anygen Diagram Generator helps agents use the AnyGen CLI and AnyGen server to turn natural-language diagram descriptions into flowcharts, architecture diagrams, sequence diagrams, mind maps, and related visual outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, product teams, and other external users use this skill to generate diagrams from structured text for architecture documentation, process review, API design, and knowledge organization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Diagram prompts and generated diagram content are sent to AnyGen's service. <br>
Mitigation: Avoid including secrets, regulated data, or sensitive proprietary architecture unless this external processing is approved. <br>
Risk: The skill uses AnyGen authentication through an API key or browser login. <br>
Mitigation: Prefer managed environment variables or browser login, and avoid pasting real API keys into chats, scripts, logs, or version control. <br>
Risk: Diagram generation depends on network access and availability of the AnyGen service. <br>
Mitigation: Confirm service access before relying on the skill in a workflow, and keep source descriptions so diagrams can be regenerated if rendering fails. <br>


## Reference(s): <br>
- [Anygen Diagram Generator on ClawHub](https://clawhub.ai/thcjp/skills/anygen-diagram-generator) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [AnyGen service](https://www.anygen.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-style execution summaries; generated diagrams may be returned as image links or downloaded files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AnyGen authentication and sends diagram prompts to AnyGen's remote service for rendering.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
