## Description: <br>
Statsig (statsig.com). Use this skill for Statsig requests that involve searching or reading project data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and product teams use this skill to inspect Statsig projects, feature gates, dynamic configs, and segments from an OOMOL-connected Statsig account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Statsig read requests may expose project configuration, gates, dynamic configs, or segments visible to the connected account. <br>
Mitigation: Review the connected Statsig project and OOMOL scopes before installation, and scope user requests to the specific objects needed. <br>
Risk: The skill routes normal Statsig requests through OOMOL connector commands even though its listed actions are read-only. <br>
Mitigation: Use the live connector schema before running actions and review command payloads for the intended project, object ID, filters, and pagination. <br>


## Reference(s): <br>
- [Statsig homepage](https://www.statsig.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-statsig) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-focused Statsig connector actions use live schemas before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
