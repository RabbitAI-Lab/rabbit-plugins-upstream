## Description: <br>
Paymo (paymoapp.com). Use this skill for ANY Paymo request - reading, creating, updating, and deleting data. Whenever a task involves Paymo, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to read and manage Paymo clients, projects, tasks, and the current authenticated user through an OOMOL-connected Paymo account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing Paymo actions can create, update, or delete clients, projects, and tasks. <br>
Mitigation: Review the exact action, target object, JSON payload, and expected effect with the user before running write actions; require explicit approval before destructive actions. <br>
Risk: The skill relies on OOMOL-brokered Paymo access and the local oo CLI. <br>
Mitigation: Install only when the user trusts OOMOL to broker Paymo access, connect the Paymo API key intentionally, and install the oo CLI only from the documented official source. <br>


## Reference(s): <br>
- [Paymo homepage](https://www.paymoapp.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
