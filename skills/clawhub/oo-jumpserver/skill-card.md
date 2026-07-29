## Description: <br>
JumpServer (jumpserver.org). Use this skill for JumpServer requests that search and read data through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect JumpServer accounts, assets, nodes, permissions, terminal sessions, and users through an OOMOL-connected JumpServer account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read infrastructure, user, permission, account, asset, node, and session records visible to the connected JumpServer account. <br>
Mitigation: Install and use it only when that visibility is intended, and ensure the connected JumpServer account has appropriate read scope. <br>
Risk: First-time setup may require installing the oo CLI, signing in to OOMOL, or connecting JumpServer. <br>
Mitigation: Review any first-time CLI installation, authentication, or account-connection step before proceeding. <br>
Risk: Future connector actions marked write or destructive could change or remove JumpServer data. <br>
Mitigation: Confirm the exact payload and effect with the user before any write action, and require explicit approval before any destructive action. <br>


## Reference(s): <br>
- [JumpServer homepage](https://www.jumpserver.org) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration guidance] <br>
**Output Format:** [Markdown with inline bash and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schemas before running JumpServer read actions; connector responses are JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
