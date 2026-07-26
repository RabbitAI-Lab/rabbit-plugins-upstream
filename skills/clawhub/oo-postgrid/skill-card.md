## Description: <br>
PostGrid enables agents to read, create, update, and delete PostGrid Print & Mail contacts and templates through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate PostGrid Print & Mail contacts and templates from an agent workflow while relying on live connector schemas before actions are run. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive actions can change or delete PostGrid contacts and templates. <br>
Mitigation: Confirm the exact action, target IDs, payload, and expected effect with the user before creating, updating, or deleting resources. <br>
Risk: The skill operates through an OOMOL-mediated connection to a PostGrid account. <br>
Mitigation: Install it only when OOMOL should mediate PostGrid actions, and use a PostGrid connection with permissions scoped to the intended work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-postgrid) <br>
- [PostGrid homepage](https://www.postgrid.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector runs may return JSON data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
