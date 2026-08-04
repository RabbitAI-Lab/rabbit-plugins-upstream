## Description: <br>
Orchestrate guarded multi-skill DeFi workflows with named recipes, quality gates, session-scoped runs, status tracking, and no key custody. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and OpenClaw agent users use this skill to plan, quality-gate, and track multi-skill DeFi workflows while leaving swaps, deposits, perps orders, and other state-changing actions to separately installed execution skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A planned DeFi workflow may include execution steps handled by separately installed skills. <br>
Mitigation: Require each execution skill to present fresh data and obtain explicit user confirmation under its own permission and confirmation flow. <br>
Risk: Workflow runs may send an agent address, session token, or optional FarmDash API key for session or paid-tier features. <br>
Mitigation: Share only the minimum required session or tier metadata, keep private keys and wallet secrets out of all calls, and treat FARMDASH_API_KEY as optional unless higher-rate features are needed. <br>
Risk: Missing companion skills can make a recipe incomplete or analysis-only. <br>
Mitigation: Classify unavailable steps before presenting a workflow as executable and continue only with the safe subset when required sub-skills are absent. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-trail-marshal) <br>
- [FarmDash Agent Hub](https://www.farmdash.one/agents) <br>
- [FarmDash API Schema](https://www.farmdash.one/agents/openapi.yaml) <br>
- [FarmDash MCP Server](https://www.farmdash.one/.well-known/mcp.json) <br>
- [FarmDash Trail Marshal Skill Source](https://www.farmdash.one/openclaw-skills/farmdash-trail-marshal/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-shaped workflow catalog, plan, run, and status data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces workflow planning and status information only; state-changing DeFi execution remains outside this skill.] <br>

## Skill Version(s): <br>
0.1.8 (source: ClawHub release metadata; artifact frontmatter reports 1.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
