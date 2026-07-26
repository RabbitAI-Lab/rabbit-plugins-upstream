## Description: <br>
Reference the workspace policy playbook, answer "What are the rules for tone, data, and collaboration?" by searching the curated policy doc or listing its sections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crimsondevil333333](https://clawhub.ai/user/crimsondevil333333) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, maintainers, and workspace collaborators use this skill to list policy sections, retrieve a policy topic, or search policy text before drafting announcements or answering policy questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The --policy-file option can read and print content from a user-supplied local file path. <br>
Mitigation: Use --policy-file only with policy documents intended for inspection, and avoid pointing it at secrets, credentials, or unrelated private files. <br>


## Reference(s): <br>
- [Workspace policies](references/policies.md) <br>
- [ClawHub skill page](https://clawhub.ai/crimsondevil333333/skills/policy-lawyer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text CLI output and Markdown documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can list policy topics, print matching policy sections, or print keyword-matched snippets.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
