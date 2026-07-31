## Description: <br>
Browser Use operates Browser Use Cloud through an OOMOL-connected account so agents can inspect sessions, run browser tasks, and retrieve account information through the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to route Browser Use Cloud tasks through an OOMOL-connected account, including session creation, session inspection, message listing, billing lookup, and controlled session stops. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or reuse Browser Use Cloud sessions and run browser tasks through the connected account. <br>
Mitigation: Confirm any task that launches or controls a browser session, especially when it could submit forms, spend credits, modify external accounts, or interact with private data. <br>
Risk: Session stop actions can change Browser Use Cloud state. <br>
Mitigation: Confirm the exact target session, payload, and expected effect with the user before running state-changing actions. <br>
Risk: The security review found the connector under-scopes browser-agent actions that can create sessions and run tasks. <br>
Mitigation: Treat browser task dispatch as a sensitive action even when it is not explicitly tagged as destructive, and review task intent before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-browser-use) <br>
- [Browser Use homepage](https://browser-use.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected Browser Use account for live actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
