## Description: <br>
Guides agents through Hetzner Cloud and dedicated-server operations, including sizing, networking, firewalls, storage, backups, costs, migration, and incident handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to plan, provision, troubleshoot, secure, and cost-manage Hetzner Cloud and Robot dedicated-server environments. It is especially useful when working with hcloud, Terraform-oriented workflows, private networking, backup design, migration, and cost review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide cloud operations that delete, rebuild, resize, detach, cancel, or otherwise change Hetzner resources. <br>
Mitigation: Review and explicitly approve any destructive or irreversible action before it is executed. <br>
Risk: The skill maintains local inventory and memory files under ~/Clawic/data/. <br>
Mitigation: Use it only where local infrastructure notes are expected, and keep tokens, passwords, keys, and rescue credentials in a secret manager rather than in those files. <br>
Risk: Command-oriented workflows may rely on the user's existing hcloud CLI or API context. <br>
Mitigation: Use scoped Hetzner projects and tokens, prefer read-only credentials for reporting, and verify the active context before approving changes. <br>


## Reference(s): <br>
- [ClawHub Hetzner skill page](https://clawhub.ai/ivangdavila/skills/hetzner) <br>
- [Clawic Hetzner skill page](https://clawic.com/skills/hetzner) <br>
- [Hetzner skill source](artifact/SKILL.md) <br>
- [Security operations guidance](artifact/security.md) <br>
- [Automation guidance](artifact/automation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline commands, code snippets, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local inventory updates under ~/Clawic/data/ and uses the hcloud CLI when command-oriented workflows apply.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
