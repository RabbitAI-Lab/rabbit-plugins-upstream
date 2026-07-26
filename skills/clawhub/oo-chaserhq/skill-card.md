## Description: <br>
ChaserHQ lets an agent search and read ChaserHQ customer, invoice, invoice history, organisation, and API status data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to retrieve ChaserHQ customer, invoice, invoice history, organisation, and status information without calling the ChaserHQ API directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer and invoice records may contain sensitive business data. <br>
Mitigation: Only request the records needed for the task and avoid exposing returned data outside the intended user or workspace. <br>
Risk: The skill depends on OOMOL authorization to read ChaserHQ data. <br>
Mitigation: Run sign-in or connection steps only when the user is ready to authorize OOMOL access, and keep credentials managed through the OOMOL connection flow. <br>


## Reference(s): <br>
- [ClawHub ChaserHQ Skill](https://clawhub.ai/oomol/skills/oo-chaserhq) <br>
- [ChaserHQ Homepage](https://www.chaserhq.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only ChaserHQ connector actions; credentials are handled through the user's OOMOL-connected account.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
