## Description: <br>
Run Fabric AI patterns for text transformation, analysis, and content creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koriyoshi2041](https://clawhub.ai/user/koriyoshi2041) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and writers use this skill to run Fabric AI patterns through the fabric-ai CLI for summarization, writing improvement, code review, threat modeling, structured extraction, and related text transformation tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Content submitted through this skill may be processed by Fabric's configured AI providers. <br>
Mitigation: Do not pass secrets, private documents, credentials, proprietary data, or private URLs unless the user accepts the configured Fabric provider handling that content. <br>
Risk: The skill depends on a local fabric-ai CLI installation and user-specific Fabric configuration. <br>
Mitigation: Confirm fabric-ai is installed and configured before use, and use dry-run or setup/update commands when validating local behavior. <br>


## Reference(s): <br>
- [Fabric Bridge on ClawHub](https://clawhub.ai/koriyoshi2041/skills/fabric-bridge) <br>
- [Fabric project](https://github.com/danielmiessler/fabric) <br>
- [Popular Fabric Patterns](references/popular-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stream Fabric CLI output and may save generated output to files when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
