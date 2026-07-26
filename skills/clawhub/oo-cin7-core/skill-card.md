## Description: <br>
Use this skill to search and read Cin7 Core data through the OOMOL cin7_core connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Cin7 Core account settings, customers, and products through an OOMOL-connected account. It supports read-only list and get workflows while relying on server-side credential handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The routing language is broad and may cause an agent to use the connector for general Cin7 Core requests. <br>
Mitigation: Give the agent explicit instructions to use this skill only when retrieving or inspecting Cin7 Core account, customer, or product data. <br>
Risk: The skill can expose connected-account business data for customers, products, and account settings. <br>
Mitigation: Install it only for agents and users that are permitted to read that Cin7 Core data through the configured OOMOL connection. <br>


## Reference(s): <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Cin7 Core homepage](https://www.cin7.com/solutions/core/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; responses include data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: artifact frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
