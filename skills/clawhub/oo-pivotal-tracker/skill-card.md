## Description: <br>
Operates Pivotal Tracker through the OOMOL pivotal_tracker connector for reading, creating, and updating projects, stories, comments, and story state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product teams, and agents with an OOMOL-connected Pivotal Tracker account use this skill to inspect projects and stories, create stories or comments, and update story state through schema-checked oo CLI connector calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Pivotal Tracker data, including creating stories, adding comments, or updating story state. <br>
Mitigation: Confirm the exact action payload and expected effect with the user before running write actions, and ensure the intended OOMOL account and Pivotal Tracker connection are active. <br>


## Reference(s): <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Pivotal Tracker](https://www.pivotaltracker.com) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches the live connector schema before constructing action payloads; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
