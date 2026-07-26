## Description: <br>
Operates Lever through an OOMOL-connected account to read opportunities, postings, and notes, and to create opportunity notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate Lever recruiting workflows through the OOMOL connector, including reading opportunities and postings and adding notes when confirmed by the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Lever opportunity records, such as adding a note. <br>
Mitigation: Require the agent to preview the exact action and payload and obtain user confirmation before running any write action. <br>
Risk: The skill has broad routing scope for Lever requests and may be selected whenever a task involves Lever. <br>
Mitigation: Install it only when the agent is expected to handle Lever tasks, and review proposed candidate, job, offer, or pipeline changes before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-lever) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Lever Homepage](https://www.lever.co) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include connector action names, schema-inspection commands, and confirmation prompts for write actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
