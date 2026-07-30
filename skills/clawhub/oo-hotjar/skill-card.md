## Description: <br>
Use this skill for Hotjar requests involving reading, creating, and updating data instead of calling the Hotjar API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate Hotjar through an OOMOL-connected account, including survey reads and user lookup requests. It guides the agent to inspect live connector schemas before sending Hotjar connector payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotjar access is mediated through OOMOL. <br>
Mitigation: Install and use the skill only when OOMOL is trusted as the intermediary for the connected Hotjar account. <br>
Risk: User lookup requests can remove matching Hotjar data when deleteAllHits is true. <br>
Mitigation: Review the exact write payload and get explicit user confirmation before running deletion-capable requests. <br>
Risk: Connector input and output contracts can change. <br>
Mitigation: Inspect the live action schema before constructing each payload. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hotjar) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Hotjar homepage](https://www.hotjar.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector execution responses are JSON when the skill runs oo connector commands with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
