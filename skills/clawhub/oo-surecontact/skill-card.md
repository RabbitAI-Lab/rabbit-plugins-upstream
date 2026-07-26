## Description: <br>
SureContact connector for reading, creating, updating, and deleting contact, list, and tag data through the OOMOL oo CLI instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage SureContact contacts, lists, tags, and memberships from an agent through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive SureContact actions can alter or delete contact, list, tag, or membership data. <br>
Mitigation: Confirm the exact payload, target identifiers, and expected effect with the user before running actions marked write or destructive. <br>
Risk: The skill depends on the OOMOL oo CLI and a persistent SureContact account connection. <br>
Mitigation: Install the CLI or connect an API key only when the user trusts OOMOL and intends to grant the agent SureContact access through that account. <br>


## Reference(s): <br>
- [SureContact homepage](https://surecontact.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads; write and destructive actions require confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
