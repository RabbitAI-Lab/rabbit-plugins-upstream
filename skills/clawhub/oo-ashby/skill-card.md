## Description: <br>
Operate Ashby through an OOMOL-connected account to read and search candidates, jobs, and API key information with the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and recruiting operations users use this skill to let an agent inspect live Ashby connector schemas and run read/search actions against Ashby data through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can query Ashby through the user's OOMOL account. <br>
Mitigation: Install and use the skill only when the user is comfortable with agent-mediated Ashby queries, and review the oo CLI setup and Ashby connection before use. <br>
Risk: Future write, delete, or overwrite actions could change Ashby data if enabled. <br>
Mitigation: Require explicit user confirmation before enabling or running any future action that writes, deletes, or overwrites Ashby data. <br>


## Reference(s): <br>
- [ClawHub Ashby skill page](https://clawhub.ai/oomol/skills/oo-ashby) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Ashby homepage](https://www.ashbyhq.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns oo CLI execution metadata when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
