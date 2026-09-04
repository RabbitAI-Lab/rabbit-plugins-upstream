## Description:

Zorus (zorustech.com). Use this skill for Zorus requests, including reading, creating, and updating data through the OOMOL connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Zorus connector schemas and run OOMOL-backed Zorus actions for customers, endpoints, groups, policies, and active unblock requests. It supports read workflows and user-confirmed state-changing connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can allow agents to access Zorus data through an OOMOL-connected account.

Mitigation: Install only when agent access to Zorus data through OOMOL is intended, and confirm the OOMOL account and connector scopes are trusted.

Risk: Write-tagged connector actions may change Zorus state if run with an incorrect payload.

Mitigation: Review payloads carefully and require user confirmation before approving any write-tagged action.

Risk: First-time CLI login or Zorus connection setup can bind the agent workflow to an unintended account or connector scope.

Mitigation: Only complete oo CLI installation, login, or Zorus connection setup when the selected OOMOL account and Zorus connection are trusted.

## Reference(s):

- [Zorus homepage](https://www.zorustech.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zorus)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
