## Description: <br>
Slab (slab.com). Use this skill for ANY Slab request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external collaborators, and developers use this skill to search, read, create, update, sync, and delete Slab workspace content through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, sync, or delete Slab content in a connected workspace. <br>
Mitigation: Review write and delete requests carefully, confirm the exact payload and target, and require explicit approval before destructive actions. <br>
Risk: First-time setup may install or run the remote OOMOL oo CLI. <br>
Mitigation: Install the CLI only if you trust OOMOL and are comfortable allowing the agent to operate through an OOMOL-connected Slab account. <br>


## Reference(s): <br>
- [Slab homepage](https://slab.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, text] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md metadata and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
