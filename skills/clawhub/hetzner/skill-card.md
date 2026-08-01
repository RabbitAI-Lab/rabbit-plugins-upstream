## Description: <br>
Hetzner helps agents plan, operate, debug, and document Hetzner Cloud and dedicated-server infrastructure, including sizing, networking, firewalls, storage, backups, costs, automation, Kubernetes, migration, and incident workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent is helping with Hetzner-specific infrastructure decisions or operations: choosing server types and regions, writing hcloud or Terraform-oriented steps, handling private networks and firewalls, planning backups and storage, reviewing costs, responding to outages or abuse notices, and recording durable local infrastructure notes. <br>

### Deployment Geography for Use: <br>
The skill can be used from any supported agent environment. Its guidance is specific to Hetzner Cloud and Robot locations and includes EU, US, and Singapore region considerations, with EU data-residency defaults when configured by the user. <br>

## Known Risks and Mitigations: <br>
Risk: The skill maintains local notes about infrastructure, projects, domains, mail, costs, incidents, and runbooks. <br>
Mitigation: Keep the configured ~/Clawic/data paths access-controlled and out of casual sync or commits; store credentials only as pointers to a keychain, password manager, CI secret store, or similar secret system. <br>
Risk: Generated plans, commands, and configuration can affect live infrastructure, billing, or destructive operations. <br>
Mitigation: Review commands before execution, verify current Hetzner prices and limits before spending money, and use the skill's snapshot, protection, and deletion checks before irreversible changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/hetzner) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Skill homepage](https://clawic.com/skills/hetzner) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Natural-language operational guidance with tables, checklists, commands, Terraform or cloud-init examples, runbook notes, and local memory updates when appropriate.] <br>
**Output Parameters:** [User requests, Hetzner context, local Clawic configuration and inventory notes, and hcloud CLI availability when command generation or inspection is needed.] <br>
**Other Properties Related to Output:** [Outputs are Hetzner-specific, cost-aware, and safety-gated; the skill is designed to avoid writing credentials and to replace secrets with secret-store pointers in durable notes.] <br>

## Skill Version(s): <br>
1.0.2 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
