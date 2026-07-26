## Description: <br>
One-install associative memory graph for any OpenClaw workspace: stage, migrate markdown memory, rewire, verify with a seeded battery, and revert. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wstienstra](https://clawhub.ai/user/wstienstra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use Engram to install and manage a local associative memory system for OpenClaw workspaces, including migration from markdown memory files, workspace rewiring, verification, and rollback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify workspace memory files and agent-instruction files. <br>
Mitigation: Review the migration dry-run report, require human approval before applying changes, and retain the backup manifest for restoration. <br>
Risk: The skill can add scheduled local jobs for backup, sleep, and verification workflows. <br>
Mitigation: Inspect scheduled job changes before install and use the uninstall path to remove ENGRAM-MANAGED cron entries. <br>
Risk: The submitted package references installer and engine scripts that are not included in the artifact evidence. <br>
Mitigation: Inspect the actual source repository and install scripts before running external installation commands. <br>


## Reference(s): <br>
- [Server-resolved GitHub repository](https://github.com/WStienstra/engram) <br>
- [ClawHub skill page](https://clawhub.ai/wstienstra/skills/engram) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces installation, migration, verification, and rollback guidance for a local workspace memory system.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
