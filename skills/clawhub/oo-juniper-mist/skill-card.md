## Description: <br>
Juniper Mist helps agents search and read Juniper Mist account, organization, site, and device information through OOMOL-connected credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, network administrators, and support agents use this skill to inspect Juniper Mist profile, organization, site, and device data from an OOMOL-connected account without calling the Juniper Mist API directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent using this skill can read Juniper Mist profile, organization, site, and device information through the connected OOMOL account. <br>
Mitigation: Install and enable it only for agents and users permitted to view that Juniper Mist data, and review OOMOL connection permissions before use. <br>
Risk: Connector commands depend on the live OOMOL action schema and account connection state. <br>
Mitigation: Inspect the connector schema before building payloads and use first-time setup steps only after an authentication, connection, or missing CLI error. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-juniper-mist) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Juniper Mist Homepage](https://www.juniper.net/us/en/products/networking/mist-ai.html) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return JSON responses from OOMOL connector actions when commands are executed with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
