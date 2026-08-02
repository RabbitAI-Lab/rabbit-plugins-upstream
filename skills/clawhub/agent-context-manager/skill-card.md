## Description: <br>
Agent Context Manager helps agents create, organize, version, and reuse AgentPMT context documents such as brand guidelines, SOPs, product facts, pricing rules, and policy documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to manage persistent AgentPMT context documents that workflows can fetch, update, archive, clone from templates, and restore from version history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can change shared operational guidance through document updates, restores, archives, or unlock workflows. <br>
Mitigation: Check the document ID and expected revision, review content before applying edits, and use account permissions carefully. <br>
Risk: Agents may rely on stale endpoint details, schemas, setup steps, or examples. <br>
Mitigation: Refresh the skill when it is more than seven days past the documented last-updated date, and fetch live schema or instructions before production integrations. <br>


## Reference(s): <br>
- [Agent Context Manager action schema](artifact/schema.md) <br>
- [AgentPMT marketplace product](https://www.agentpmt.com/marketplace/agent-context-manager) <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/agent-context-manager) <br>
- [agentpmt publisher profile](https://clawhub.ai/user/agentpmt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, API calls, JSON, markdown] <br>
**Output Format:** [Markdown guidance with JSON request examples and action schemas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No local command runtime is declared; calls rely on AgentPMT-hosted remote tools.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
