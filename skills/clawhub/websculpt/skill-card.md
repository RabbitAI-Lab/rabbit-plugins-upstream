## Description: <br>
WebSculpt bootstraps browser automation with a reusable command library by installing or repairing the WebSculpt CLI and routing agents to lifecycle skills for exploration, capture, maintenance, and library management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bqw1013](https://clawhub.ai/user/bqw1013) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, analysts, content operators, and ecommerce teams use this skill to set up WebSculpt when they need browser automation, web data acquisition, API calls, scraping, or reusable commands for repeated web workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install persistent global tooling and lifecycle skills across multiple agent skill directories. <br>
Mitigation: Install only when persistent WebSculpt behavior is desired, and prefer project-local installation when the workflow should stay scoped to one project. <br>
Risk: The default global setup can modify skill directories under the user's home folder. <br>
Mitigation: Review the installation scope and installed files before allowing global setup or later updates. <br>
Risk: Browser automation and scraping workflows may access logged-in or content-gated web data. <br>
Mitigation: Use WebSculpt only for accounts, sites, and data sources the user is authorized to access, and review generated commands before reuse. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bqw1013/skills/websculpt) <br>
- [Skill documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and routing instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May install persistent global or project-local WebSculpt tooling and lifecycle skill files depending on user intent and environment state.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
