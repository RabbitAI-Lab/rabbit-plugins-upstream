## Description:

Diagnose OpenClaw Android, iOS, or macOS node pairing, QR/setup code, route, auth, and connection failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose OpenClaw node-to-gateway connectivity, setup code, route, authentication, and pairing failures across Android, iOS, and macOS clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device approval guidance could authorize the wrong OpenClaw device if a pending request is accepted without confirming the request ID.

Mitigation: Treat every openclaw devices approve command as state-changing; approve only a request ID confirmed out of band as belonging to the intended device, and do not approve pairings automatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/node-connect)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagnostic questions, command sequences, and route-specific remediation steps.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
