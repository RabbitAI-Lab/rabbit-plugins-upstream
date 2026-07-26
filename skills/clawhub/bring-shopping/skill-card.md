## Description: <br>
Manage Bring! shopping lists via the unofficial bring-shopping Node.js library using email/password login for listing lists, reading items, adding or removing items, and checking or unchecking items when API-style access is acceptable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cutzenfriend](https://clawhub.ai/user/cutzenfriend) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to manage Bring! shopping lists from an agent by running explicit CLI commands for list lookup, item reads, and item updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Bring account credentials to access shopping lists. <br>
Mitigation: Install only if you are comfortable giving the skill Bring credentials, and store BRING_EMAIL and BRING_PASSWORD in environment configuration rather than bundling them with the skill. <br>
Risk: Write actions can add, remove, check, or uncheck items on the selected Bring list. <br>
Mitigation: Specify the target list for write actions and review add, remove, check, and uncheck requests before running them. <br>
Risk: The skill depends on the unofficial bring-shopping npm package. <br>
Mitigation: Pin or review the bring-shopping dependency before using the skill with a real account. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; CLI responses are JSON or short status text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BRING_EMAIL and BRING_PASSWORD environment variables and explicit command arguments for list and item operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
