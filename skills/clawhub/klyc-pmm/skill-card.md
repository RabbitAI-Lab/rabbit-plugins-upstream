## Description: <br>
KLYC-PMM provides scripts for AI-agent memory initialization, cloud-backed push, search, recovery, local file watching, distillation, and systemd-based persistence using curl and jq. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sylncn](https://clawhub.ai/user/sylncn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to give an AI agent persistent text memory across sessions, including memory push, search, disaster recovery, watched-file synchronization, and local readiness checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload memory and identity-related workspace files to kunlunyaochi.com. <br>
Mitigation: Use it only in workspaces approved for that cloud memory service, review watched files before syncing, and keep secrets out of MEMORY.md, SOUL.md, IDENTITY.md, AGENTS.md, USER.md, and TOOLS.md. <br>
Risk: The one-click and daemon installers may install dependencies, write local configuration, and set up a persistent watcher that can require root or systemd access. <br>
Mitigation: Run read-only checks such as quickstart.sh and self-test first, review the scripts, and require explicit approval before running oneclick.sh or install-daemon.sh in sensitive environments. <br>
Risk: Persistent watch mode can continue syncing file changes after initial setup. <br>
Mitigation: Limit the watched file list to intended files, verify the configured API endpoint, and stop or disable the service when continuous synchronization is not required. <br>
Risk: Recovery tokens can restore cloud-backed memory and may expose sensitive history if shared. <br>
Mitigation: Store recovery tokens in an approved secret store, avoid placing them in public logs or shared documents, and rotate or reinitialize access if a token is exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sylncn/skills/klyc-pmm) <br>
- [PMM full architecture](references/pmm-full-architecture.md) <br>
- [Examples README](examples/README.md) <br>
- [KLYC-PMM service documentation](https://kunlunyaochi.com/?route=klyc-pmm) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and shell-oriented terminal output with local configuration files and JSON recovery data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The scripts may create or update local memory, identity, token, index, service, and recovery files.] <br>

## Skill Version(s): <br>
8.3.8 (source: frontmatter, skill.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
