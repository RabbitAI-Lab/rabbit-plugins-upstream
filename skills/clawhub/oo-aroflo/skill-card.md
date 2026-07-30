## Description: <br>
AroFlo helps agents search and read AroFlo business data through an OOMOL-connected account using the oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when an agent needs to retrieve AroFlo clients, tasks, users, or API health information through an authenticated OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose AroFlo business data through a connected OOMOL account. <br>
Mitigation: Install and use it only when the intended agent should read AroFlo data, and review OOMOL and AroFlo access scopes before connecting. <br>
Risk: First-time setup may run a remote oo CLI installer. <br>
Mitigation: Run the installer only when the oo CLI is missing and only if the installer source is trusted. <br>
Risk: If future AroFlo actions are marked write or destructive, they could change or remove AroFlo records. <br>
Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval before destructive actions. <br>


## Reference(s): <br>
- [AroFlo homepage](https://aroflo.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aroflo) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [AroFlo icon](https://static.oomol.com/logo/third-party/aroflo.svg) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses from connector actions are JSON objects containing data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
