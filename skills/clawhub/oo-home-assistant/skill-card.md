## Description:

Home Assistant (home-assistant.io). Use this skill for ANY Home Assistant request: reading, creating, updating, and deleting data through the OOMOL-connected Home Assistant connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Home Assistant schemas, read states and logs, and control or configure connected Home Assistant entities through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing Home Assistant actions can affect devices, scripts, automations, services, events, or configuration.

Mitigation: Confirm the exact payload and expected effect before call_service, execute_script, fire_event, write, or destructive actions, especially for locks, alarms, climate, doors, appliances, and broad automation events.

Risk: Remote installer commands pipe downloaded scripts directly into bash or PowerShell.

Mitigation: Avoid running the curl-to-bash or PowerShell iex installer automatically; prefer a verified and pinned installation method for the oo CLI.

Risk: Some configuration actions require admin access and only cover UI-managed Home Assistant entries.

Mitigation: Inspect the live action schema before submitting requests, verify administrative scope, and confirm the target automation, scene, or script before creating, replacing, or deleting it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-home-assistant)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Home Assistant Homepage](https://www.home-assistant.io)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Home Assistant Connection Settings](https://console.oomol.com/app-connections?provider=home_assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI commands against the user's connected Home Assistant account when the hosting agent has permission.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
