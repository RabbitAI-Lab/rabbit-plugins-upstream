## Description: <br>
Access recipes, meal plans, and grocery lists from Paprika Recipe Manager. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mjrussell](https://clawhub.ai/user/mjrussell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to query a Paprika Recipe Manager account for recipes, meal plans, grocery lists, and cooking-related lookup tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to access personal recipes, meal plans, and grocery lists from a Paprika account. <br>
Mitigation: Install and use it only where access to that account data is intended, and review returned account data before sharing it elsewhere. <br>
Risk: Authentication can use Paprika credentials in environment variables, which may be exposed in shared shells or logs. <br>
Mitigation: Prefer interactive `paprika auth` when possible and avoid storing Paprika passwords in shared shell history, logs, or multi-user environments. <br>
Risk: The skill depends on the external `paprika` CLI being installed from npm. <br>
Mitigation: Verify the npm package source before global installation and keep normal dependency review practices in place. <br>


## Reference(s): <br>
- [Paprika Recipe Manager](https://www.paprikaapp.com) <br>
- [ClawHub Paprika Skill](https://clawhub.ai/mjrussell/skills/paprika) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON-producing CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can request JSON output from the Paprika CLI for programmatic recipe, meal, and grocery-list data.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
