## Description: <br>
Guides users through Socratic SOP discovery, then produces AS-IS and TO-BE workflow diagrams, automation recommendations, and personalized OpenClaw configuration files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwei03804-a11y](https://clawhub.ai/user/wwei03804-a11y) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and operations-focused users use this skill to document repetitive work processes, identify automation opportunities, and generate reviewable configuration files for an OpenClaw-style agent setup. It is intended for workflow analysis and planning, not direct execution of automation or professional consulting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may enter passwords, API keys, customer secrets, or confidential business details while describing their workflows. <br>
Mitigation: Do not provide secrets or confidential details; keep sensitive values out of prompts and fill them manually only after review. <br>
Risk: Suggested install commands or package sources may not be appropriate for a user's environment. <br>
Mitigation: Verify each package, source, and command before execution, and prefer a staged test environment for installation. <br>
Risk: Generated OpenClaw configuration files could overwrite or change an existing agent setup. <br>
Mitigation: Back up existing configuration and review generated AGENTS.md, TOOLS.md, HEARTBEAT.md, and IDENTITY.md before merging changes. <br>
Risk: Recommended third-party skills are not guaranteed to be available, secure, or suitable. <br>
Mitigation: Review security scores, download signals, source information, and behavior before adopting any recommended skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wwei03804-a11y/skills/ai-replace-me-check) <br>
- [Output File Guide](references/output-guide.md) <br>
- [Example Outputs](references/example-outputs.md) <br>
- [Mermaid Diagram Template](references/mermaid-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with ASCII diagrams, tables, code blocks, shell commands, and generated configuration file content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are generated from the user's answers and may include SOUL.md, USER.md, AGENTS.md, TOOLS.md, HEARTBEAT.md, IDENTITY.md, skill recommendations, and a custom skill creation prompt when no suitable SkillHub result is found.] <br>

## Skill Version(s): <br>
2.3.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
