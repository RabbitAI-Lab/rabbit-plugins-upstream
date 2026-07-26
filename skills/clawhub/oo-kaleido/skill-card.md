## Description: <br>
Kaleido helps agents search and read Kaleido account data through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Kaleido consortia, memberships, environments, nodes, and services from an OOMOL-connected Kaleido account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The oo CLI can access data in the user's connected Kaleido account. <br>
Mitigation: Install and use the skill only for an intended OOMOL-connected Kaleido account. <br>
Risk: Future write or destructive connector actions could modify or remove Kaleido resources. <br>
Mitigation: Review the action target and payload explicitly before approving any write or destructive action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kaleido) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Kaleido homepage](https://www.kaleido.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill instructs agents to inspect the live connector schema before running Kaleido actions and to return JSON responses from the oo CLI when actions are executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
