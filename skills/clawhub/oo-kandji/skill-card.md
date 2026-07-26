## Description: <br>
Use Iru (Kandji) for requests that search and read data through the Kandji connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect the live Kandji connector schema, then run read-only Kandji blueprint and directory-user lookup or listing actions through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an OOMOL-connected Kandji account to read blueprint and directory-user data. <br>
Mitigation: Install and run it only when you trust oomol and intend the agent to use the connected Kandji account for read-only lookups. <br>
Risk: Future versions could add Kandji actions that change or remove data. <br>
Mitigation: Before any write action, confirm the exact payload and effect with the user; before any destructive action, require explicit approval for the target. <br>
Risk: Authentication, connection, scope, credential, or billing failures may require setup steps outside the normal read-only action flow. <br>
Mitigation: Run setup, connection, or billing commands only after a command fails with the matching error. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kandji) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Iru (Kandji) homepage](https://www.iru.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The agent should inspect the live connector schema before constructing payloads; the listed actions are read-only get and list operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
