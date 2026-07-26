## Description: <br>
Demodesk helps agents search and read Demodesk recordings, transcripts, summaries, scorecards, and users through an OOMOL-connected oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to retrieve Demodesk account data such as recordings, transcripts, summaries, scorecards, and visible users through a connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may cause an agent to query Demodesk when the user only intended to discuss Demodesk. <br>
Mitigation: For vague Demodesk mentions, explicitly tell the agent whether to query Demodesk or only discuss it. <br>
Risk: The skill can read data from the connected Demodesk account through OOMOL. <br>
Mitigation: Install and enable it only when account data access through OOMOL is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-demodesk) <br>
- [Demodesk homepage](https://demodesk.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
