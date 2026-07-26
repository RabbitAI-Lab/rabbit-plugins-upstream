## Description: <br>
Ordinal (tryordinal.com) connector for reading, creating, and updating workspace data through OOMOL's oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate an OOMOL-connected Ordinal workspace from an agent, including reading workspace records and preparing confirmed write actions through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First-time setup includes pipe-to-shell installer commands that execute downloaded code on the user's machine. <br>
Mitigation: Use installer commands only after oo is missing, and review OOMOL's official installation guidance before running them. <br>
Risk: Connector actions can affect Ordinal workspace data when an action is marked write or destructive. <br>
Mitigation: Fetch the live action schema first and confirm the exact payload and expected effect with the user before write or destructive actions. <br>
Risk: The skill runs oo connector commands against a connected Ordinal workspace and may return workspace data. <br>
Mitigation: Run commands only for the user's intended workspace task and rely on OOMOL-managed credentials rather than handling raw tokens. <br>


## Reference(s): <br>
- [Ordinal homepage](https://www.tryordinal.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI installation guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ordinal) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON when actions are run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
