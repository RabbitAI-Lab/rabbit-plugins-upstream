## Description:

Use Coil's CLI and API for agent-operated outbound recipes, durable runs, lead management, automations, provider integrations, feedback, and runtime discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agent operators use this skill to install, authenticate, discover, and operate Coil workflows through the supported CLI and API. It supports outbound recipes, durable runs, lead and scrape management, automations, provider integrations, SmartLead actions, feedback, and runtime discovery against the same organization state used in the Coil dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through actions that access organization data, export leads, create provider-backed runs, send leads to SmartLead, or mutate integrations.

Mitigation: Install only for intended Coil usage, review high-impact commands before execution, require explicit provider spend confirmation, and keep human-admin approval for publish, delete, policy, and ambiguous-effect changes.

Risk: Coil API keys and provider credentials can expose organization data or connected services if copied into command arguments, logs, issue bodies, or recipe inputs.

Mitigation: Provide secrets through a runtime secret manager or stdin, prefer profile-based authentication, and avoid placing credentials in persistent text or command-line arguments.

## Reference(s):

- [Coil API Endpoints](references/api-endpoints.md)
- [Coil API Fields](references/api-fields.md)
- [Coil Homepage](https://www.usecoil.com)
- [ClawHub Skill Page](https://clawhub.ai/doubledipcode/skills/coil-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline shell commands, CLI examples, and API reference tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers JSON CLI output, profile-based authentication, and stdin or secret-manager handling for credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
