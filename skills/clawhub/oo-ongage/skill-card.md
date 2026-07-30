## Description: <br>
Ongage helps agents read, create, and update Ongage data through the OOMOL oo CLI connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs to inspect Ongage lists or contacts and prepare confirmed contact updates through an OOMOL-connected Ongage account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can update Ongage contact status or contact records. <br>
Mitigation: Confirm the exact payload and expected effect with the user before approving contact status changes, updates, or upserts. <br>
Risk: The skill operates through an OOMOL-connected Ongage account. <br>
Mitigation: Install or connect the oo CLI only when needed, and use an account with appropriate Ongage access for the task. <br>
Risk: Action input and output contracts may differ from assumptions in a prompt. <br>
Mitigation: Fetch the live action schema with oo connector schema before building each payload. <br>


## Reference(s): <br>
- [ClawHub Ongage Skill](https://clawhub.ai/oomol/skills/oo-ongage) <br>
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [Ongage Homepage](https://www.ongage.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include oo CLI JSON responses with data and meta.executionId when actions run.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
