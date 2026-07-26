## Description: <br>
Perdoo lets agents read, create, and update Perdoo data through OOMOL's oo CLI connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to work with Perdoo goals, filters, progress updates, and GraphQL operations from an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Perdoo GraphQL operations can include mutations that change workspace data. <br>
Mitigation: Require explicit user confirmation for execute_graphql mutations and any operation that changes Perdoo data. <br>
Risk: The skill can access sensitive company goals or metrics from a connected Perdoo workspace. <br>
Mitigation: Review the skill before installation and limit use to appropriately authorized Perdoo accounts. <br>


## Reference(s): <br>
- [Perdoo homepage](https://www.perdoo.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before building payloads and returns connector responses as JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
