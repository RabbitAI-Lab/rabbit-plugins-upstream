## Description: <br>
Fly.io (fly.io). Use this skill for Fly.io requests covering reading, creating, and updating data through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect and manage Fly.io apps and Machines through an OOMOL-connected account. It supports read operations and confirmed Machine lifecycle changes such as create, start, stop, restart, and wait. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, start, stop, or restart Fly.io Machines, which changes live Fly.io state. <br>
Mitigation: Review every write action payload and confirm the exact effect with the user before execution. <br>
Risk: Using the skill depends on OOMOL-connected Fly.io credentials. <br>
Mitigation: Install it only when the user intends to manage Fly.io through OOMOL and is comfortable with that credential path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fly) <br>
- [Fly.io homepage](https://fly.io/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and require live schema inspection before action payloads are constructed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
