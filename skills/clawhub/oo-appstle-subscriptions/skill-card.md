## Description: <br>
Appstle Subscriptions (appstle.com). Use this skill for Appstle Subscriptions requests that search or read customer and subscription data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Appstle Subscriptions customer and subscription records through the OOMOL oo CLI. It supports read-only lookup workflows such as retrieving customer subscription details, valid subscription contract IDs, and paginated customer subscription lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Appstle customer and subscription data through the user's OOMOL account. <br>
Mitigation: Install and use it only for accounts where that read access is intended, and review returned customer or subscription data before sharing it further. <br>
Risk: Connector action schemas may change over time. <br>
Mitigation: Inspect the live action schema with `oo connector schema` before constructing payloads. <br>
Risk: First-time CLI login and Appstle connection steps affect account-level access. <br>
Mitigation: Perform install, login, billing, and Appstle connection recovery steps deliberately, only after a command fails for the matching setup reason. <br>


## Reference(s): <br>
- [Appstle Subscriptions homepage](https://appstle.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-appstle-subscriptions) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
