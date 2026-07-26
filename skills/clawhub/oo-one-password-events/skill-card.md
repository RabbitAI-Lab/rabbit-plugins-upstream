## Description: <br>
Helps agents query 1Password Events API audit events, item usage events, and sign-in attempts through OOMOL's oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent retrieve read-only 1Password Events API logs for audit review, item usage analysis, and sign-in investigation through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: 1Password event logs may reveal sensitive account activity even when accessed through read-only actions. <br>
Mitigation: Install and use the skill only with an OOMOL-connected account whose 1Password Events API access is appropriate for the user's audit or investigation task. <br>
Risk: Connector calls can fail or expose authorization gaps when the oo CLI is not installed, the user is not signed in, the connection is missing, or billing is unavailable. <br>
Mitigation: Follow the skill's setup and recovery guidance only after a command fails with the matching authentication, connection, scope, credential, or billing error. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-one-password-events) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [1Password Events API homepage](https://1password.com) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides read-only connector calls and returns command output from the oo CLI, typically JSON data with execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
