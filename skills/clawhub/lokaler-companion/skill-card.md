## Description:

Builds a local monitoring companion application that runs on 127.0.0.1, polls configured sources, records state changes, and can provide starter scripts, a PWA, optional browser extension, and container guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kikikari](https://clawhub.ai/user/kikikari)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build local companion apps that monitor public or permitted sources, keep state locally, and notify users when a meaningful status change occurs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated companion may start a local Python server, poll configured sources, and save logs or state on the user's machine.

Mitigation: Confirm the local behavior before installation, keep the server bound to 127.0.0.1 unless broader access is intentional, and review local logs and state files as part of deployment.

Risk: An optional browser extension can request host permissions for monitored sites.

Mitigation: Grant host permissions only for the exact sites being monitored, and avoid private or access-controlled resources unless explicit permission exists.

Risk: Container deployment can expose a monitoring service beyond the local machine if ports are published broadly.

Mitigation: Publish container ports to 127.0.0.1 by default and broaden network exposure only after an explicit access-control review.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/kikikari/skills/lokaler-companion)
- [Dauerbetrieb im Container](references/docker.md)
- [Browser-Erweiterung (Manifest V3)](references/erweiterung.md)
- [Installierbare Oberflaeche (PWA)](references/pwa.md)
- [Der Starter](references/starter.md)
- [Fallstricke](references/fallstricke.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks and helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local server, starter, PWA, browser extension, or container configuration artifacts depending on the requested companion app.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
