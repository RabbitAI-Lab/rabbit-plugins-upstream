## Description: <br>
Ringover helps agents use the oo CLI to search and read Ringover calls, users, groups, IVRs, numbers, tags, and team data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to retrieve Ringover call, user, group, IVR, number, tag, and team information from an OOMOL-connected account. Review before installation because the security evidence flags write-capable instructions despite the read/search framing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence says the read/search framing conflicts with write-capable instructions and broad Ringover routing language. <br>
Mitigation: Review the exact supported operations before installation and require explicit confirmation before any account, contact, call, message, or other state-changing action. <br>
Risk: Ringover actions can expose account data allowed by the connected API key. <br>
Mitigation: Use a least-privilege Ringover token where possible and inspect the live action schema before executing commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ringover) <br>
- [Ringover homepage](https://www.ringover.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
