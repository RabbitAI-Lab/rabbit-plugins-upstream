## Description:

Intuiface lets agents list running Intuiface experiences and send Web Trigger messages through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and teams use this skill to operate Intuiface through an OOMOL-connected account, including listing available running experiences and sending confirmed Web Trigger messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes mutable remote installer one-liners for the oo CLI.

Mitigation: Use a reviewed and verified OOMOL CLI installation path; do not allow an agent to run remote installer one-liners unless the source is trusted.

Risk: The send_message action can change Intuiface state by sending Web Trigger messages to running experiences.

Mitigation: Confirm the exact target experiences, payload, and expected effect with the user before running write actions.

Risk: Intuiface request and response data may be sensitive when routed through OOMOL.

Mitigation: Assess the sensitivity of payloads and responses before using the connector, and avoid sending confidential data unless the routing is approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-intuiface)
- [Intuiface homepage](https://www.intuiface.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
