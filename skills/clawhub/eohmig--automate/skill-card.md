## Description:

Use this skill to create Codex Automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to prepare new Codex Automations interactively: it clarifies triggers, tools, instructions, integration settings, and approval before handing the draft to the Automations editor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Created automations can later act through connected services such as Slack, repositories, PagerDuty, Linear, Sentry, or MCP integrations.

Mitigation: Review the draft trigger, tools, integration settings, and deferred editor fields before approving and opening the Automations editor.

Risk: A draft with unresolved integration settings may not reflect the user's intended channel, repository, service, team, or project.

Mitigation: Resolve picker-backed integration values through discovery when available, or explicitly defer them for final selection in the editor.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/automate)
- [Cloud Agent dashboard](https://cursor.com/dashboard?tab=cloud-agents)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Plain-language guidance with a compact Markdown draft table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include resolved integration settings and editor handoff notes; YAML or JSON is shown only when requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
