## Description: <br>
DevOps helps agents design, repair, and harden software delivery systems across CI/CD, releases, environments, reliability, on-call, infrastructure workflow, and operational recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, SREs, and delivery teams use this skill to plan and troubleshoot pipelines, release strategies, rollback plans, environment parity, SLOs, incidents, capacity, recovery, and supply-chain practices. It is intended for delivery-system design and operational guidance rather than product-specific workflow syntax. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can maintain local operational notes and remove rows it previously wrote under configured Clawic paths. <br>
Mitigation: Install only when that local note maintenance is desired, keep backups for important operational notes, and review file changes that affect durable records. <br>
Risk: Pasted pipeline files, environment data, Terraform output, or incident logs may contain secret values. <br>
Mitigation: Store secret references such as environment-variable, vault, password-manager, SSM, or file pointers instead of plaintext credentials. <br>
Risk: DevOps guidance can affect production delivery, reliability, access, or rollback behavior. <br>
Mitigation: Treat recommendations as proposals for review, require explicit confirmation before destructive operations, and prefer reversible release and infrastructure changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/devops) <br>
- [Clawic skill homepage](https://clawic.com/skills/devops) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline code, configuration snippets, shell commands, plans, checklists, and local note-file updates when applicable.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update local Clawic operational memory files under configured paths; secret values are intended to be stored as pointers, not plaintext credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
