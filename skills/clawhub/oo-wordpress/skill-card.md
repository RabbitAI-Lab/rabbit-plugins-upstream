## Description: <br>
Operate a connected WordPress account through OOMOL's wordpress connector to read, create, update, and delete WordPress content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content operators use this skill to manage WordPress sites from an agent, including listing and reading content and preparing confirmed create, update, or delete actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive WordPress actions can change or delete site content. <br>
Mitigation: Confirm the exact payload, expected effect, and target IDs before create, update, or delete actions. <br>
Risk: The skill depends on the third-party oo CLI, an OOMOL account connection, and server-side WordPress credentials. <br>
Mitigation: Install and use it only when the user intends to trust OOMOL with the connected WordPress account. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-wordpress) <br>
- [WordPress](https://wordpress.org) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an authenticated OOMOL account, connected WordPress credentials, and live action schemas from the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
