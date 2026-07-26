## Description: <br>
Guides an agent to search and read Podscribe data through an OOMOL-connected account using the oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to inspect Podscribe integration health, retrieve show information, or search episodes through a connected Podscribe account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be selected broadly for Podscribe-related requests and could prompt account setup steps. <br>
Mitigation: Only install the oo CLI, sign in, or connect Podscribe when the user intentionally wants that account connected or an action fails for the matching reason. <br>
Risk: Connector actions depend on account state, scopes, billing, and live action schemas. <br>
Mitigation: Fetch the current action schema before sending payloads and surface authentication, connection, scope, or billing failures to the user before retrying. <br>


## Reference(s): <br>
- [Podscribe homepage](https://podscribe.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-podscribe) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Directs the agent to fetch live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
