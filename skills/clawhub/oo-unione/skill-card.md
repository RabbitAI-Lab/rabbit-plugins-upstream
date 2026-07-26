## Description: <br>
UniOne (unione.io). Use this skill for ANY UniOne request — reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect UniOne account data, list suppressions, tags, and templates, and send transactional email through an OOMOL-connected UniOne account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: UniOne access is mediated through an OOMOL-connected account and the oo CLI. <br>
Mitigation: Install and use the skill only when the user trusts OOMOL, the oo CLI, and the connected account configuration. <br>
Risk: The send_email action can send transactional email from the user's UniOne account. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running write actions. <br>
Risk: Authentication, connection, or billing recovery steps may change account state or require external setup. <br>
Mitigation: Run setup or recovery commands only after a matching command failure and user consent. <br>


## Reference(s): <br>
- [UniOne homepage](https://unione.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-unione) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include oo CLI command output in JSON when actions are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
