## Description: <br>
Pinata (pinata.cloud). Use this skill for Pinata requests, including reading, creating, updating, and deleting data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate Pinata through the OOMOL oo CLI, including file and group reads, group management, pin-by-CID workflows, metadata updates, and controlled destructive actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive Pinata actions can create, update, remove, or overwrite Pinata data. <br>
Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive commands. <br>
Risk: The skill can operate a user's Pinata account through an OOMOL-connected account. <br>
Mitigation: Install and use it only when the user intends to let the agent operate that Pinata account through OOMOL. <br>
Risk: First-time setup may use a remote oo CLI installer if the CLI is not already installed. <br>
Mitigation: Prefer an already installed oo CLI where available, and review the installer source before approving remote installation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pinata) <br>
- [Pinata Homepage](https://pinata.cloud) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses from the connector include data and meta.executionId when actions are run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
