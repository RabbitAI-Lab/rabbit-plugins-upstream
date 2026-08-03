## Description: <br>
cloudbase guides agents through developing, designing, deploying, debugging, and troubleshooting CloudBase projects across Web, WeChat Mini Programs, databases, cloud functions, CloudRun, storage, AI models, agents, operations, and specs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build and operate CloudBase applications, configure auth, database, storage, cloud function, CloudRun, AI, and deployment workflows, and route agent work to scenario-specific CloudBase references. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation rules and CloudBase management guidance could lead an agent into high-impact cloud actions outside a tightly scoped request. <br>
Mitigation: Use the skill only for real CloudBase projects, require an explicit target EnvId, and require confirmation before deployment, billing-impacting operations, or global plugin installation. <br>
Risk: Weak authentication examples could be copied into production code. <br>
Mitigation: Treat examples as illustrative only; require real token validation and avoid shared anonymous identities before production use. <br>
Risk: AI and observability workflows may expose prompts, raw user identifiers, or third-party data flows. <br>
Mitigation: Avoid logging raw user identifiers or prompts, and review third-party AI and observability data flows before enabling those features. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase) <br>
- [CloudBase main skill](artifact/SKILL.md) <br>
- [Activation map](artifact/references/activation-map.yaml) <br>
- [MCP setup](artifact/references/mcp-setup.md) <br>
- [Deployment workflow](artifact/references/deployment-workflow.md) <br>
- [CloudBase platform guide](artifact/references/cloudbase-platform/SKILL.md) <br>
- [CloudBase code review guide](artifact/references/cloudbase-code-review/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent toward CloudBase MCP or mcporter actions; such actions should remain explicitly scoped to the target EnvId and confirmed before deployment or billing impact.] <br>

## Skill Version(s): <br>
1.92.39 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
