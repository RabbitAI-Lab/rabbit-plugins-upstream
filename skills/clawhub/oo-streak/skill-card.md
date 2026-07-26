## Description: <br>
Streak (streak.com). Use this skill for Streak requests that involve searching and reading data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business users use this skill to read Streak boxes, pipelines, and current-user information through an OOMOL-connected Streak account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read Streak data visible to the connected OOMOL account. <br>
Mitigation: Connect only the intended Streak account and review requested read operations before use. <br>
Risk: The first-time setup path installs and uses the third-party oo CLI. <br>
Mitigation: Run the remote install step only when the CLI is needed and OOMOL is trusted in the deployment environment. <br>
Risk: Connector input contracts may change over time. <br>
Mitigation: Inspect the live connector schema before each action and build payloads from that schema. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-streak) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Streak homepage](https://www.streak.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing Streak action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
