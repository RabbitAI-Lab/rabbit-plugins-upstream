## Description:

Use Coil's CLI and API for agent-operated outbound recipes, durable runs, lead management, automations, provider integrations, feedback, and runtime discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and operators use this skill to let agents install, authenticate, discover, and operate Coil through the same organization state humans use in the dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can operate authenticated Coil workspace workflows and provider-backed actions.

Mitigation: Install only if you trust Coil and intend to let an agent operate your Coil workspace; review provider-spend commands before running them.

Risk: API keys, provider tokens, cookies, and other secrets could be exposed through command arguments, logs, issue bodies, or recipe inputs.

Mitigation: Use scoped secrets through a runtime secret manager or stdin, keep cookies and API keys out of logs, and avoid placing secrets in recipe inputs.

Risk: Publication, policy decisions, reconciliation, and other high-impact actions require human authority.

Mitigation: Rely on Coil's human review and publish handoffs, relay server-provided human_action URLs verbatim, and do not treat those URLs as approval or authority.

## Reference(s):

- [Coil homepage](https://www.usecoil.com)
- [ClawHub skill page](https://clawhub.ai/doubledipcode/skills/coil-api)
- [Coil API Endpoints](references/api-endpoints.md)
- [Coil API Fields](references/api-fields.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON/API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routine operations prefer the Coil CLI with --json output and server-provided human handoffs relayed verbatim.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
