## Description: <br>
Wise (wise.com). Use this skill for searching and reading Wise data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to retrieve Wise exchange rates, supported currencies, and available personal or business profiles from a connected Wise account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands run against the connected Wise account and can return account profile or currency data. <br>
Mitigation: Use the intended OOMOL account and Wise connection, keep credentials least-privilege, and avoid sharing sensitive returned data. <br>
Risk: Future connector actions tagged as write or destructive could change Wise state. <br>
Mitigation: Confirm the exact action, target, and JSON payload with the user before running actions tagged write or destructive. <br>
Risk: First-time setup may require installing the oo CLI before the skill can run actions. <br>
Mitigation: Run setup only after a matching command failure and use the referenced OOMOL install guide. <br>


## Reference(s): <br>
- [Wise homepage](https://wise.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches the live connector schema before constructing action payloads; documented actions are read-only.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
