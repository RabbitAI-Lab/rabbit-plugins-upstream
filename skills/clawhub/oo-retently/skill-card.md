## Description: <br>
Retently (retently.com) supports reading, creating, and updating Retently data through an OOMOL-connected account instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Retently account, campaign, customer, feedback, and template data, and to create or update Retently customers through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Retently data through OOMOL-connected credentials. <br>
Mitigation: Install and use it only for trusted OOMOL and Retently accounts, and rely on OOMOL server-side credential handling rather than exposing raw tokens. <br>
Risk: Bulk customer upserts can create or update Retently customer records. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running write actions. <br>
Risk: Authentication, connection, or billing setup commands can change account state or require external trust decisions. <br>
Mitigation: Run setup or connection steps only after an action fails for the matching reason and the user approves the step. <br>


## Reference(s): <br>
- [Retently homepage](https://www.retently.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns Retently connector responses as JSON when commands are run.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
