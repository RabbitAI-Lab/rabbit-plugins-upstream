## Description: <br>
Helps agents operate rented virtual private servers end to end, including provider and plan selection, first boot, access recovery, snapshots, resizing, networking, migration, incidents, and cost review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and technical users use this skill for practical VPS administration decisions and recovery workflows across rented servers. It guides provider selection, provisioning, access recovery, firewalls, backups, resizing, migration, incidents, outbound mail, and cost control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update local Clawic VPS, server, domain, and finance records during normal use. <br>
Mitigation: Ask the agent to show a diff and get confirmation before changing local infrastructure records. <br>
Risk: VPS operations can include destructive or irreversible actions such as rebuilds, destroys, disk growth, address release, snapshot deletion, or firewall enablement. <br>
Mitigation: Require the agent to state the blast radius, fallback path, and explicit confirmation before running or recommending those actions. <br>
Risk: Infrastructure records could accidentally capture secrets if the user asks to save private keys, passwords, or API tokens. <br>
Mitigation: Store only credential pointers such as file, keychain, password-manager, or environment-variable references, not credential values. <br>


## Reference(s): <br>
- [ClawHub VPS skill page](https://clawhub.ai/ivangdavila/skills/vps) <br>
- [Clawic VPS skill page](https://clawic.com/skills/vps) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands, operational checklists, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local infrastructure-record updates under Clawic data paths; should avoid storing credentials and request confirmation for destructive or irreversible operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
