## Description: <br>
Manage recipes, meal plans, and shopping lists in Tandoor Recipe Manager. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itsnikhil](https://clawhub.ai/user/itsnikhil) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent search, create, retrieve, and schedule recipes in a configured Tandoor Recipe Manager instance. It also supports browsing reference data and managing shopping-list items through authenticated command-line calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a configured Tandoor API token that can read and change recipes, meal plans, and shopping-list data. <br>
Mitigation: Use the least-privileged token available, keep TANDOOR_API_TOKEN out of chat and logs, and verify TANDOOR_URL points to the intended Tandoor server. <br>
Risk: Create, schedule, check-off, and delete operations can modify personal recipe, meal-plan, or shopping-list data. <br>
Mitigation: Require the agent to confirm exact recipes, dates, meal types, quantities, and item IDs before making mutations. <br>


## Reference(s): <br>
- [Tandoor API Quick Reference](references/API.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/itsnikhil/skills/tandoor-recipes) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON or text command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node, TANDOOR_URL, and TANDOOR_API_TOKEN.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
