## Description: <br>
Manage Cargo connectors and integrations from the Cargo CLI, including listing, creating, updating, removing, and inspecting connector actions for workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage authenticated Cargo connectors and discover integration actions needed to configure workflow nodes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connector configuration values, API keys, OAuth tokens, and command output may contain secrets. <br>
Mitigation: Treat connector configs and CLI output as sensitive; avoid putting production keys in shell history or shared logs. <br>
Risk: Connector create, update, and remove commands can mutate authenticated Cargo connector instances. <br>
Mitigation: Verify the active Cargo session, connector UUIDs, and connector usage counts before changing or removing connectors. <br>


## Reference(s): <br>
- [Cargo Skill Page](https://clawhub.ai/cargo-ai/skills/cargo-connection) <br>
- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills) <br>
- [Cargo CLI - Connections](SKILL.md) <br>
- [Connector examples](references/examples/connectors.md) <br>
- [Integration examples](references/examples/integrations.md) <br>
- [Response shapes](references/response-shapes.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Cargo CLI command examples and JSON response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires @cargo-ai/cli and a Cargo account authenticated by browser sign-in or API token.] <br>

## Skill Version(s): <br>
1.2.0 (source: SKILL.md frontmatter, skill-metadata.json, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
