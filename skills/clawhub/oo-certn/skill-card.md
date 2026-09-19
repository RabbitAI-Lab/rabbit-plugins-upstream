## Description:

Certn helps agents read Certn background-check cases, groups, users, packages, questionnaires, tags, and events through an OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations users use this skill to retrieve Certn background-check and account resources through an existing OOMOL connection. It is designed for read-only case, group, user, event, package, questionnaire, and tag lookup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands that execute changing code on the local machine.

Mitigation: Install the oo CLI only through a verified, pinned, or signed method, and do not allow an agent to run curl|bash or irm|iex setup commands automatically.

Risk: The skill can read background-check and user-related Certn data available through the connected OOMOL account.

Mitigation: Confirm the connected Certn account and scopes before use, and apply least-privilege access for users who can invoke the skill.

Risk: Certn data is accessed through OOMOL as an intermediary.

Mitigation: Install only when the organization is comfortable with OOMOL mediating access to Certn data and can control the setup process.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-certn)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Certn Homepage](https://certn.co)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from Certn connector actions when commands are executed.]

## Skill Version(s):

1.0.3 (source: server evidence release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
