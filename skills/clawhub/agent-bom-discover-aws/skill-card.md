## Description: <br>
Discover AWS-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived cloud credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud security engineers use this skill to inventory AWS Bedrock, ECS, SageMaker, Lambda, EKS, Step Functions, EC2, and related agentic infrastructure as canonical agent-bom inventory. It supports local discovery and optional local scanning only when the operator explicitly requests it. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on AWS access from the operator environment. <br>
Mitigation: Use read-only AWS profiles or short-lived roles scoped to only the intended accounts, regions, and services. <br>
Risk: Generated inventory can contain sensitive infrastructure details. <br>
Mitigation: Store and share inventory and scan outputs carefully, and write them only to operator-selected local paths. <br>
Risk: The workflow can invoke the external agent-bom package for scanning. <br>
Mitigation: Confirm trust in the agent-bom package before installation or execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws) <br>
- [agent-bom source repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and operator-selected JSON inventory output paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local canonical inventory JSON and optional local scan/export files only to operator-selected paths.] <br>

## Skill Version(s): <br>
0.98.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
