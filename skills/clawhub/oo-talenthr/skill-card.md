## Description:

TalentHR connector skill for reading, creating, and updating TalentHR data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operators use this skill to let an agent operate TalentHR through an OOMOL-connected account, including role changes that update TalentHR state. The agent should inspect the live connector schema before building action payloads and confirm write effects with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change a TalentHR employee role through a scoped write action.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running role-change commands.

Risk: The first-time setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Prefer the official install guide or inspect installer scripts before execution.

Risk: Using the skill gives an agent access through the user's OOMOL-connected TalentHR account.

Mitigation: Install and use it only when the user intends the agent to operate that TalentHR account.

## Reference(s):

- [TalentHR homepage](https://www.talenthr.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-talenthr)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and returns connector responses as JSON when actions run.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
