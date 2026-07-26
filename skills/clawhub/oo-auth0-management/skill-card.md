## Description: <br>
Auth0 Management (auth0.com). Use this skill for ANY Auth0 Management request: reading, creating, updating, and deleting data through the OOMOL Auth0 Management connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, administrators, and support teams use this skill to inspect Auth0 users, roles, and permissions and to make confirmed role or permission changes through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Auth0 role or permission assignments. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running actions tagged as write. <br>
Risk: Destructive actions can remove Auth0 access by removing roles or permissions. <br>
Mitigation: Require explicit approval for the target and payload before running actions tagged as destructive. <br>
Risk: Connector credentials and scopes may be missing, expired, or insufficient. <br>
Mitigation: Use first-time setup or reconnection steps only after a command fails with an authentication, scope, credential, or connection error. <br>


## Reference(s): <br>
- [Auth0 Management homepage](https://auth0.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-auth0-management) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API Calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing Auth0 Management payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
