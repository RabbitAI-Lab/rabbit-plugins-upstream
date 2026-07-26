## Description: <br>
Paradym (paradym.id) lets an agent read, create, and update Paradym data through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents connected to an OOMOL account use this skill to inspect Paradym schemas and run Paradym connector actions for OpenID4VC issuance, verification, projects, templates, sessions, and issued credential metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create Paradym credential offers or verification requests. <br>
Mitigation: Inspect the live action schema first and confirm the exact payload and intended effect with the user before running write actions. <br>
Risk: The skill operates a user's Paradym account through OOMOL-managed credentials. <br>
Mitigation: Use it only when the user wants OOMOL-connected Paradym access, and perform one-time oo CLI or app-connection setup only from trusted sources when an auth or connection error requires it. <br>


## Reference(s): <br>
- [ClawHub Paradym skill listing](https://clawhub.ai/oomol/skills/oo-paradym) <br>
- [Paradym homepage](https://paradym.id) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The agent should inspect the live connector schema before constructing payloads and should present write payloads for user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
