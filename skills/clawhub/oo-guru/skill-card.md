## Description: <br>
Guru (getguru.com) skill for searching and reading Guru cards, collections, identity, and team statistics through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search and read Guru workspace content visible to their connected OOMOL account, including cards, collections, identity, and team statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Guru search and read results may expose private workspace knowledge visible to the connected account. <br>
Mitigation: Use the skill only with accounts whose Guru access is appropriate for the task, and avoid sharing returned content outside authorized contexts. <br>
Risk: The skill depends on OOMOL-managed Guru connectivity and server-side credential handling. <br>
Mitigation: Complete the oo CLI and OOMOL connection setup only when OOMOL is trusted for the Guru integration. <br>


## Reference(s): <br>
- [Guru homepage](https://www.getguru.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent to inspect live connector schemas before running Guru read and search actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
