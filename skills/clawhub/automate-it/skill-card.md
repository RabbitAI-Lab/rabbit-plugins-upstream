## Description: <br>
Create content tasks and automations in Automate It, do the content work yourself or leave it to the built-in worker, poll task status through the human review gate, and fetch links to published posts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workingdevshero](https://clawhub.ai/user/workingdevshero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content operators, and agents use this skill to draft, schedule, publish, and monitor Automate It content tasks through a scoped API key and a human review workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A broadly scoped API key could permit more task, content, automation, or file actions than the current job needs. <br>
Mitigation: Use a narrowly scoped Automate It API key for the specific task and report missing-scope errors instead of retrying with broader access by default. <br>
Risk: Reviewer/admin actions and --no-review can bypass or alter the normal human review workflow. <br>
Mitigation: Use reviewer/admin commands or --no-review only when the operator explicitly requests them, and do not approve or publish content produced by the same agent. <br>
Risk: Deletion commands and some automation or folder operations can permanently affect workspace data. <br>
Mitigation: Require an explicit operator deletion request before passing --yes, and prefer non-destructive updates such as revising content in place. <br>


## Reference(s): <br>
- [Automate It agents homepage](https://automate.it.com/agents) <br>
- [ClawHub skill page](https://clawhub.ai/workingdevshero/skills/automate-it) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node and an Automate It API key; command effects are bounded by API key scopes and workspace role.] <br>

## Skill Version(s): <br>
0.4.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
