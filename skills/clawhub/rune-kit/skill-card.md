## Description: <br>
Rune is a 66-skill mesh for AI coding assistants that routes code, review, deployment, documentation, research, and domain-extension workflows through connected agent skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nhadaututtheky](https://clawhub.ai/user/nhadaututtheky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use Rune to coordinate coding-agent workflows for implementation, debugging, review, testing, deployment, documentation, and project recovery. The package is most useful when an agent needs structured routing across many software delivery tasks rather than a single narrow helper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill kit can mutate repositories and create persistent project context files such as .rune artifacts and CLAUDE.md. <br>
Mitigation: Install and invoke it only in repositories where those writes are acceptable, and review generated files before relying on them in later sessions. <br>
Risk: Some workflows can propose or run dependency changes, commits, pushes, releases, and production deploys. <br>
Mitigation: Require explicit user approval for those actions and keep test, security, rollback, and deployment gates enabled before production use. <br>
Risk: External CLI/model calls and messaging workflows can expose data or send unintended messages if controls are weak. <br>
Mitigation: Require confirmation for external calls and messaging actions, and avoid the Zalo messaging path until confirmation and rate limiting are enforced in the tool handler. <br>


## Reference(s): <br>
- [ClawHub Rune skill page](https://clawhub.ai/nhadaututtheky/skills/rune-kit) <br>
- [Rune documentation](https://rune-kit.github.io/rune) <br>
- [Rune guides](https://rune-kit.github.io/rune/guides) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, command suggestions, generated files, reports, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write project context, plans, reports, documentation, deployment notes, and other workflow artifacts when the invoked Rune skill calls for file output.] <br>

## Skill Version(s): <br>
2.29.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
