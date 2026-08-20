## Description:

Enables an agent to work with DACHSER shipment and delivery-order information through the OOMOL DACHSER connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect DACHSER delivery-order status, shipment history, and current shipment status through a connected OOMOL DACHSER account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a connected OOMOL DACHSER account, including an action marked [write].

Mitigation: Install it only when agent access to that account is intended, and review the exact payload and expected effect before any [write] action.

Risk: Setup and login commands can alter the local agent environment or account connection state.

Mitigation: Run CLI installation, authentication, or reconnection steps only as recovery steps after a matching command failure.

## Reference(s):

- [DACHSER homepage](https://www.dachser.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dachser)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL oo CLI schema checks before connector actions; action responses are expected as JSON from the connector.]

## Skill Version(s):

1.0.0 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
