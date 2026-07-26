## Description: <br>
Codegen (codegen.com). Use this skill for ANY Codegen request -- searching and reading data. Whenever a task involves Codegen, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect Codegen action schemas and run read-only Codegen connector actions through an OOMOL-connected account for organizations, repositories, users, and agent runs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read Codegen account information exposed through the user's OOMOL connection, including organizations, repositories, users, and agent runs. <br>
Mitigation: Install only when that account-level access is acceptable, and review the oo CLI setup and OOMOL connection steps before first use. <br>
Risk: The skill depends on the local oo CLI, OOMOL authentication, a valid Codegen connection, and available OOMOL credit. <br>
Mitigation: Follow the documented recovery paths for missing CLI, authentication, connection scope, expired credential, app readiness, and billing errors. <br>


## Reference(s): <br>
- [Codegen homepage](https://codegen.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-codegen) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live action schemas before request construction and returns connector data with execution metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
