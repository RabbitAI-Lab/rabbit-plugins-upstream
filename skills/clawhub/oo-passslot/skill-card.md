## Description: <br>
PassSlot helps agents read, create, update, and delete PassSlot Wallet pass data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Apple Wallet passes in PassSlot through an OOMOL-connected account. It supports listing pass types, templates, and passes; retrieving pass URLs and values; creating passes from templates; updating placeholder values; and deleting passes after explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or update Wallet passes in the connected PassSlot account. <br>
Mitigation: Confirm the target pass, requested payload, and intended effect with the user before running write actions. <br>
Risk: The delete_pass action permanently deletes a PassSlot Wallet pass. <br>
Mitigation: Require explicit user approval for the specific pass before running destructive actions. <br>
Risk: Commands require an installed and authenticated oo CLI with a connected PassSlot account. <br>
Mitigation: Use setup steps only after an auth or connection failure, and rely on OOMOL-managed credentials instead of exposing raw tokens. <br>


## Reference(s): <br>
- [PassSlot homepage](https://www.passslot.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub PassSlot skill](https://clawhub.ai/oomol/skills/oo-passslot) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON when commands use the --json flag.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
