## Description: <br>
Orchestrates AgentLoop evaluation workflows through the Aliyun CLI plugin with safe previews, saved evaluator and evaluator-skill management, one-shot sample tests, trace or dataset batch runs, polling, and result inspection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare, preview, execute, monitor, and analyze Alibaba Cloud AgentLoop evaluation workflows while preserving explicit confirmation for cloud mutations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or change Alibaba Cloud AgentLoop resources and may incur cloud costs. <br>
Mitigation: Use least-privilege RAM credentials and require the documented dry-run preview plus explicit user confirmation before any --execute action. <br>
Risk: Evaluation result or analysis JSON may include customer or business data. <br>
Mitigation: Store outputs in a private path and include raw content only when it is necessary and explicitly authorized. <br>
Risk: CLI and plugin installation or update steps affect the local execution environment. <br>
Mitigation: Review setup scripts before running them and prefer the documented Aliyun CLI and plugin update commands. <br>


## Reference(s): <br>
- [ClawHub Skill Release](https://clawhub.ai/sdk-team/skills/alibabacloud-agentloop-evaluation) <br>
- [Workflow Specification](references/spec-format.md) <br>
- [AgentLoop Evaluation API Map](references/api-map.md) <br>
- [Evaluation Result Analysis](references/result-analysis.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [RAM Policies](references/ram-policies.md) <br>
- [Alibaba Cloud CLI Installation Guide](references/cli-installation-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON workflow specifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create JSON spec, result, and analysis files; cloud mutations require dry-run preview and explicit confirmation.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
