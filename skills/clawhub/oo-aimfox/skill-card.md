## Description: <br>
Aimfox lets agents operate Aimfox through an OOMOL-connected account for reading, creating, updating, and deleting Aimfox data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers who use Aimfox with OOMOL use this skill to inspect campaigns, leads, metrics, interactions, and labels, and to manage campaign audiences through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write or destructive Aimfox actions can change campaign audiences or remove campaign profiles. <br>
Mitigation: Confirm the exact payload, target, and expected effect with the user before running tagged write or destructive actions. <br>
Risk: Aimfox action payloads are sent through the OOMOL oo connector and depend on the user's connected Aimfox account. <br>
Mitigation: Install and use this skill only for OOMOL-connected Aimfox workflows, and review each requested action payload before approval. <br>
Risk: The oo CLI installer and connector toolchain must be trusted before use. <br>
Mitigation: Run the OOMOL CLI installer only when the user trusts that toolchain and needs the CLI for Aimfox access. <br>


## Reference(s): <br>
- [Aimfox homepage](https://aimfox.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub Aimfox skill listing](https://clawhub.ai/oomol/skills/oo-aimfox) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the oo connector schema before action payloads; write and destructive Aimfox actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
