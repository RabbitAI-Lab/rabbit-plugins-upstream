## Description: <br>
Nango helps agents read, create, update, and delete Nango data through the OOMOL oo CLI connector instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Nango connections, integrations, and provider configurations from an OOMOL-connected account. It supports read operations plus confirmed tag, metadata, and deletion workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requests that retrieve connection details may expose credentials when the connected account permits it. <br>
Mitigation: Review retrieval requests for need and scope before running them. <br>
Risk: Write and destructive actions can modify tags, replace metadata, or delete Nango connections. <br>
Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before execution. <br>
Risk: First-time setup commands can install tools, authenticate accounts, or open connection flows. <br>
Mitigation: Run setup only after a command fails with the matching installation, authentication, connection, or billing error. <br>


## Reference(s): <br>
- [Nango homepage](https://nango.dev) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nango) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration guidance, JSON responses] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
