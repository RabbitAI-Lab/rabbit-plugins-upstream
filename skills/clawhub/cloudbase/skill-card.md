## Description: <br>
CloudBase helps agents develop, design, build, deploy, debug, migrate, and troubleshoot CloudBase projects across Web, WeChat Mini Programs, mobile apps, databases, cloud functions, CloudRun, storage, AI integrations, operations, and specification workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route CloudBase implementation work to the right specialized guidance, prepare backend resources, implement frontend and backend changes, and review CloudBase projects before completion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents using this skill may perform broad CloudBase management, deployment, deletion, or permission changes. <br>
Mitigation: Require explicit human confirmation before deploy, delete, permission, or other cloud-resource management actions. <br>
Risk: Included examples may encourage weak authentication patterns if copied directly into production. <br>
Mitigation: Review authentication examples before use and replace weak patterns with production-appropriate provider, session, and permission controls. <br>
Risk: Cloud logs, telemetry, third-party LLM calls, or conversation storage may expose sensitive project or user data. <br>
Mitigation: Add project-specific privacy controls for logging, telemetry, model calls, and conversation persistence before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase) <br>
- [CloudBase main entry raw source](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md) <br>
- [Activation map](references/activation-map.yaml) <br>
- [MCP setup](references/mcp-setup.md) <br>
- [Deployment workflow](references/deployment-workflow.md) <br>
- [CloudBase code review rules index](references/cloudbase-code-review/references/RULES_INDEX.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with code, shell commands, and configuration snippets as needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to read packaged reference files before acting on CloudBase tasks.] <br>

## Skill Version(s): <br>
1.92.31 (source: ClawHub release metadata; artifact frontmatter version: 2.25.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
