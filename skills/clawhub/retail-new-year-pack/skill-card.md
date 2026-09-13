## Description:

Turn seller-supplied new-year store mood notes into one retail playlist of 8 to 15 instrumentals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External retail sellers and their agents use this skill to plan and generate a reusable New Year instrumental playlist for storefront playback, with live pricing confirmation before billable Beatra music generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra Device Token with access beyond music generation.

Mitigation: Install only if broad Beatra account access is acceptable, keep the token in the documented private credential file, and avoid exposing it in chat, logs, command arguments, or environment variables.

Risk: The bundled client can silently update package-owned files automatically.

Mitigation: Review the release before installation and disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when silent replacement is not acceptable.

Risk: The generic Beatra call interface could be used outside the documented retail playlist workflow.

Mitigation: Limit use to the documented Beatra tools and package workflows, and avoid arbitrary Beatra tool calls through the generic client interface.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/retail-new-year-pack)
- [Beatra skill homepage](https://beatra.ai/skills/retail-new-year-pack)
- [New-year retail playlist workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate paid Beatra text-to-music generation after user confirmation; reports task IDs, returned artifacts, durations, and net charged credits from Beatra task responses.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
