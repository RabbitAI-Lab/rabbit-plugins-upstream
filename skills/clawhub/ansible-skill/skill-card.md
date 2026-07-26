## Description: <br>
Infrastructure automation with Ansible for server provisioning, configuration management, application deployment, and multi-host orchestration, including playbooks for OpenClaw VPS setup, security hardening, and common server configurations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[botond-rackhost](https://clawhub.ai/user/botond-rackhost) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to operate Ansible-based server automation, including base system setup, SSH and firewall hardening, Node.js installation, and OpenClaw deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled inventories and playbooks can change remote systems if run casually. <br>
Mitigation: Review and replace inventory targets before execution, then use --list-hosts, --check, --diff, and --limit to constrain runs. <br>
Risk: SSH and firewall hardening can interrupt access to a server. <br>
Mitigation: Verify console or out-of-band access before applying SSH or firewall changes. <br>
Risk: Passwordless sudo and third-party package sources may be unsuitable for production defaults. <br>
Mitigation: Reconsider passwordless sudo and pin or verify third-party package sources before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/botond-rackhost/skills/ansible-skill) <br>
- [Ansible best practices](references/best-practices.md) <br>
- [Ansible modules cheatsheet](references/modules-cheatsheet.md) <br>
- [Ansible troubleshooting guide](references/troubleshooting.md) <br>
- [Ansible Documentation](https://docs.ansible.com/) <br>
- [Ansible Galaxy](https://galaxy.ansible.com/) <br>
- [geerlingguy Ansible roles](https://github.com/geerlingguy?tab=repositories&q=ansible-role) <br>
- [Ansible for DevOps](https://www.ansiblefordevops.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with YAML and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ansible and ansible-playbook binaries; includes runnable inventories, playbooks, and roles that can modify remote systems.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
