## Description: <br>
Builds Hugo blogs optimized for agent readers with minimal HTML, no JavaScript, structured metadata, RSS, nginx configuration, and maintenance scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byron-mckeeby](https://clawhub.ai/user/byron-mckeeby) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and site operators use this skill to create and operate Hugo blogs that are easy for AI agents to parse, including theme setup, content templates, RSS output, nginx configuration, and validation scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes nginx configuration and sudo/systemctl reload examples that can affect a live server if run without review. <br>
Mitigation: Review the nginx configuration and administrative commands, test them in a non-production environment, and run privileged commands only with explicit operator approval. <br>
Risk: The setup flow pulls an external Hugo theme source into the blog project. <br>
Mitigation: Review and pin the external theme source before deployment, and keep dependency updates under source control. <br>
Risk: The validation examples use curl against a target domain. <br>
Mitigation: Run network validation only against domains you own or have permission to test. <br>


## Reference(s): <br>
- [Hugo Ananke Theme](https://github.com/theNewDynamic/gohugo-theme-ananke) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell, TOML, HTML, YAML, nginx, and XML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes setup guidance, generated file examples, server configuration examples, and validation commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
