## Description: <br>
FDE guides forward deployed engineers through enterprise AI deployment by mapping workflows, identifying AI nodes, preparing delivery materials, and planning sofagent installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kongfangxun](https://clawhub.ai/user/kongfangxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Forward deployed engineers, enterprise operators, and technical teams use this skill to run a staged enterprise AI deployment workflow: gather business context, map workflows, identify and quantify AI nodes, produce delivery documentation, and prepare sofagent-backed rollout steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer delegates to sofagent/scripts/install.sh and may install persistent agent infrastructure. <br>
Mitigation: Review the delegated installer before use, confirm whether it creates hooks or daemons, and test installation in a disposable environment before enterprise deployment. <br>
Risk: The skill workflow records enterprise workflow and audit data, and security evidence flags uncertainty about .sofagent storage, retention, and redaction. <br>
Mitigation: Define storage and retention rules before rollout, verify redaction with representative sensitive or regulated data, and restrict collected content to what the deployment needs. <br>
Risk: Audit results can be forwarded to external chat webhooks after deployment. <br>
Mitigation: Use only approved webhook destinations, inspect the audit payload before enabling forwarding, and avoid sending secrets or regulated data through chat integrations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/fde) <br>
- [FDE deployment manual](FDE.md) <br>
- [FDE README](README.md) <br>
- [Quick start guide](quick-start.md) <br>
- [Deployment plan template](templates/deployment-plan.md) <br>
- [Enterprise profile template](templates/enterprise-profile.md) <br>
- [OpenFDE workflow](https://open-fde.com/docs/workflow) <br>
- [OpenFDE Agent era](https://open-fde.com/zh/docs/agent-era) <br>
- [OpenFDE white paper](https://open-fde.com/zh/white-book) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with checklists, templates, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces staged deployment artifacts such as enterprise profiles, deployment plans, node definitions, skill templates, and quick-start guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
