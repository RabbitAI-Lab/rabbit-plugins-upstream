## Description: <br>
Searches AgentPMT's public site and catalog so agents can find official marketplace, workflow, agent, documentation, article, paper, video, page, and FAQ results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill to search AgentPMT's public catalog and content, route users to relevant tools, workflows, agents, and docs, and ground answers in official AgentPMT URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search text may be sent to AgentPMT public catalog and content endpoints. <br>
Mitigation: Keep queries narrow and do not include account secrets, wallet keys, mnemonics, signatures, or payment headers in prompts or logs. <br>
Risk: The skill searches AgentPMT public site and catalog surfaces only, not the general web. <br>
Mitigation: Use it only for AgentPMT resources and fetch live schema or instructions before production integrations when parameters or outputs are unclear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/agentpmt-docs-and-content) <br>
- [AgentPMT marketplace page](https://www.agentpmt.com/marketplace/agentpmt-docs-and-content) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Markdown guidance with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns AgentPMT public search results and tool-call guidance; user-directed search text may be sent to AgentPMT APIs.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
