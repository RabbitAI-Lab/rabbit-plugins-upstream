## Description: <br>
FDE Agent helps agents structure enterprise AI deployments, enforce task gates, run compliance audits, maintain local knowledge, and coordinate sofagent subagents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kongfangxun](https://clawhub.ai/user/kongfangxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, enterprise IT teams, and implementation engineers use this skill to plan sofagent/FDE deployments, map workflows into AI nodes, build local rule and knowledge layers, audit deployment health, and guide ongoing optimization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delegate work to shell-run subagents and sofagent CLI tools. <br>
Mitigation: Review proposed commands before execution, run with least privilege in the intended workspace, and require user confirmation for high-impact actions. <br>
Risk: The skill can persist broad local work records, knowledge, audit reports, and custom rule files. <br>
Mitigation: Review what will be stored, avoid secrets or unnecessary personal data, and keep task logs and knowledge files redacted. <br>
Risk: USB creation or deployment actions can write to the wrong target device or path. <br>
Mitigation: Before running deployment or USB creation commands, require an explicit final confirmation naming the exact platform, target device, and path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent) <br>
- [Agency Agents Chinese templates](https://github.com/jnMetaCode/agency-agents-zh) <br>
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI command examples and configuration or file-update instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to create or update local sofagent task logs, knowledge files, custom rules, deployment notes, audit reports, and USB deployment artifacts.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
