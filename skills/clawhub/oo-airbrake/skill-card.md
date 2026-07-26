## Description: <br>
Airbrake helps agents inspect Airbrake projects, deploys, error groups, notices, and notice statuses through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to inspect Airbrake projects, deploys, error groups, notices, and notice processing status through an OOMOL-connected Airbrake account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates through an OOMOL-connected Airbrake account, so granted Airbrake scopes determine what the agent can access. <br>
Mitigation: Install it only for intended Airbrake use, review granted scopes, and keep the Airbrake connection limited to the access the workflow requires. <br>
Risk: Actions marked write or destructive could change Airbrake state if run with an incorrect payload or target. <br>
Mitigation: Inspect the live connector schema before building payloads and require explicit user confirmation before any action marked write or destructive. <br>


## Reference(s): <br>
- [Airbrake homepage](https://airbrake.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-airbrake) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides live schema inspection before connector actions and returns connector results as JSON when actions are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
