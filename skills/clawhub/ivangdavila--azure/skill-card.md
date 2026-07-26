## Description: <br>
Azure helps agents architect, debug, secure, operate, and cost-optimize Azure infrastructure across compute, networking, identity, storage, databases, monitoring, governance, and infrastructure as code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud engineers, and operators use this skill to plan and review Azure deployments, diagnose platform failures, reduce spend, harden cloud exposure, and produce Azure CLI, KQL, IaC, and runbook guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can ask an agent to persist and reorganize local Azure operational records under ~/Clawic/data, including inventory, spend, contacts, and incident or runbook notes. <br>
Mitigation: Protect the directory, review generated files periodically, and require the agent to show diffs or ask for confirmation before writing, moving, or deleting records. <br>
Risk: Some guidance can affect live Azure resources, cost, access, or availability when converted into CLI or infrastructure-as-code changes. <br>
Mitigation: Keep commands read-only by default, name the subscription and region, state cost and blast radius, preview IaC changes, and require explicit confirmation before destructive operations. <br>


## Reference(s): <br>
- [Azure skill on ClawHub](https://clawhub.ai/ivangdavila/skills/azure) <br>
- [Azure skill homepage](https://clawic.com/skills/azure) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline Azure CLI, KQL, Bicep, ARM, and Terraform snippets when applicable] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local files under ~/Clawic/data/azure/ for preferences, memory, inventory, spend history, and runbooks; credentials are represented only as pointers.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
