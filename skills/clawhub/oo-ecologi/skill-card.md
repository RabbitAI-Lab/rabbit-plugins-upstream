## Description: <br>
Enables agents to operate Ecologi through an OOMOL-connected account for reading impact totals and running supported purchase actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect Ecologi account impact totals and execute supported Ecologi purchase actions through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Purchase actions can spend money or create billable Ecologi activity. <br>
Mitigation: Require explicit user confirmation of the exact purchase payload, quantity, and expected cost before any purchase_* action is run. <br>
Risk: Security evidence says the skill under-discloses billable purchase actions and treats untagged actions as safe reads. <br>
Mitigation: Review the action name before execution and treat all purchase_* actions as write actions even when the source skill does not tag them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ecologi) <br>
- [Ecologi Homepage](https://ecologi.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL Ecologi Connection](https://console.oomol.com/app-connections?provider=ecologi) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute live connector actions that return JSON responses with execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
