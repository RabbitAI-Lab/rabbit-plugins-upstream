## Description: <br>
Affinda helps an agent read, create, and update Affinda data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect Affinda connector schemas, list or retrieve Affinda resources, and upload documents from URLs through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create documents in the connected Affinda account. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running document creation actions. <br>
Risk: The skill depends on OOMOL CLI installation, sign-in, and an Affinda account connection with server-side credential injection. <br>
Mitigation: Install or connect accounts only when the user trusts OOMOL and intends to let an agent operate the Affinda account. <br>
Risk: Connector input or output contracts may change over time. <br>
Mitigation: Inspect the live connector schema before constructing payloads for each action. <br>


## Reference(s): <br>
- [Affinda ClawHub listing](https://clawhub.ai/oomol/skills/oo-affinda) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Affinda homepage](https://www.affinda.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schemas before action execution; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
