## Description: <br>
KLYC-PMM provides persistent AI-agent memory workflows for initialization, memory capture, recovery, local and remote search, file watching, paid upgrades, and HTTPS API communication using curl and jq. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sylncn](https://clawhub.ai/user/sylncn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to persist text memories, recover an agent memory state from a recovery token, search local or hosted memory, and configure watcher or daemon workflows for ongoing synchronization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can transmit memory, identity, and workspace file content to a remote service. <br>
Mitigation: Review the watched file list and API endpoint before use, and keep secrets out of watched memory or identity files. <br>
Risk: The skill can install or run a long-running watcher or systemd service. <br>
Mitigation: Inspect daemon installation commands, run without root where possible, and confirm the uninstall or disable path before enabling persistence. <br>
Risk: Paid upgrade flows depend on external payment behavior. <br>
Mitigation: Confirm the payment endpoint, order retry behavior, and expected user confirmation flow before running upgrade commands. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/sylncn/skills/klyc-pmm) <br>
- [PMM full architecture](artifact/klyc-pmm/references/pmm-full-architecture.md) <br>
- [Pay Skill packaging standard](artifact/klyc-pmm/references/pay-skill-spec.md) <br>
- [Skill manifest](artifact/klyc-pmm/skill.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and shell-oriented text with JSON configuration and command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local memory/configuration files, watcher state, and systemd service definitions when users run the provided scripts.] <br>

## Skill Version(s): <br>
9.1.9 (source: frontmatter, skill.json, CHANGELOG, and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
