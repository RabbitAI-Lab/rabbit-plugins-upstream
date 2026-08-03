## Description: <br>
Discovers AWS-hosted AI agent and MCP-relevant assets with operator-approved AWS credentials, writes canonical agent-bom inventory JSON, and can optionally scan or export that inventory locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers, security engineers, and platform operators use this skill to inventory AWS-hosted agentic infrastructure across services such as Bedrock, ECS, SageMaker, Lambda, EKS, Step Functions, and EC2. It is designed for discovery-first workflows where inventory is written locally and any scan, export, or handoff is operator-approved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AWS credentials and generated inventory may expose account access patterns or sensitive infrastructure metadata if the scope is too broad. <br>
Mitigation: Use short-lived read-only AWS credentials and narrow the account, region, service set, and output path to the audit need. <br>
Risk: Credential values could be accidentally shared if pasted into prompts or printed during troubleshooting. <br>
Mitigation: Use the existing AWS SDK credential chain and do not request, paste, or display raw AWS access keys, session tokens, or bearer tokens. <br>
Risk: Optional scan, export, or push steps can move inventory beyond the discovery-only boundary. <br>
Mitigation: Run only discovery by default and require explicit operator approval for scans, exports, destination URLs, authentication methods, and retained evidence classes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws) <br>
- [agent-bom GitHub Homepage](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI Package](https://pypi.org/project/agent-bom/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON inventory outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local, operator-selected inventory and scan output paths; no hidden persistence or telemetry was found in the provided security evidence.] <br>

## Skill Version(s): <br>
0.98.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
