## Description: <br>
Azure helps agents architect, debug, secure, operate, migrate, and cost-optimize Azure infrastructure across compute, identity, networking, storage, databases, monitoring, infrastructure as code, and production operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and operators use this skill to plan Azure architectures, diagnose platform failures, control spend, harden identity and network exposure, generate Azure CLI and IaC guidance, and maintain local operational notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill keeps local Azure operational notes, including inventory and review records, under ~/Clawic/data/. <br>
Mitigation: Protect ~/Clawic/data/ like internal infrastructure documentation and review announced writes. <br>
Risk: Azure credentials or secrets could be exposed if a user asks the agent to save pasted secret values. <br>
Mitigation: Do not paste secrets for storage; use secret pointers such as Key Vault, environment variables, keychain entries, or password-manager references. <br>
Risk: Azure operations can affect live infrastructure or cost. <br>
Mitigation: Review proposed commands and require explicit confirmation before destructive actions such as delete, purge, force, Complete-mode deployment, or lock removal. <br>


## Reference(s): <br>
- [ClawHub Azure Skill Page](https://clawhub.ai/ivangdavila/skills/azure) <br>
- [Clawic Azure Skill Page](https://clawic.com/skills/azure) <br>
- [Azure Skill Definition](artifact/SKILL.md) <br>
- [Azure Security Guidance](artifact/security.md) <br>
- [Azure CLI Command Guidance](artifact/commands.md) <br>
- [Local Memory Template](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Azure CLI, KQL, Bicep, ARM, Terraform, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Azure reads and local note updates under configured Clawic data paths; destructive Azure actions require explicit confirmation.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
