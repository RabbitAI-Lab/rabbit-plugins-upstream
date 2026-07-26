## Description: <br>
ConfigCat (configcat.com). Use this skill for ANY ConfigCat request - searching and reading data. Whenever a task involves ConfigCat, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect ConfigCat products, configs, environments, feature flags, settings, and setting values through an OOMOL-connected ConfigCat account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query ConfigCat data available to the user's OOMOL-connected credentials. <br>
Mitigation: Use it only with the intended OOMOL account and ConfigCat connection, and avoid sharing returned configuration or flag data beyond the authorized context. <br>
Risk: One-time CLI installation, login, and connector setup steps depend on trusting OOMOL and the local execution environment. <br>
Mitigation: Run setup commands only when an action fails with the matching authentication, connection, or missing CLI error. <br>


## Reference(s): <br>
- [ConfigCat homepage](https://configcat.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schema output before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
