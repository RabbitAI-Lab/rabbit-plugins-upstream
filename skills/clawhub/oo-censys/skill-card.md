## Description:

Censys (censys.com). Use this skill for Censys requests that search or read Censys Global Data assets through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security analysts use this skill to retrieve Censys certificate, host, and web property records through the oo CLI after inspecting the live action schema for the requested action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could be unsafe if an agent runs them automatically.

Mitigation: Do not let an agent run curl|bash or irm|iex installer commands. Install the oo CLI yourself from a trusted source and verify the installer or package where possible.

Risk: The connected Censys account determines what data the skill can access.

Mitigation: Connect only the Censys account intended for this skill and review account scope before use.

## Reference(s):

- [Censys homepage](https://censys.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Censys skill page](https://clawhub.ai/oomol/skills/oo-censys)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses from the connector]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
