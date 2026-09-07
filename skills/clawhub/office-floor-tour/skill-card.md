## Description:

Turn seller-supplied office floor stills into one office floor tour clip per labeled still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External real estate listing teams and agents use this skill to turn named office floor stills into one short floor walkthrough clip per still, with a free shot list before paid video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad Beatra account access through a shared local device token.

Mitigation: Authorize only accounts where video generation, wallet spending, and related media-generation access are acceptable; revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The bundled client stores Beatra connection state under ~/.beatra.

Mitigation: Keep the credential file private to the local user and avoid copying tokens into chat, logs, command arguments, environment variables, or backups.

Risk: Automatic package updates are enabled by default and run silently before ordinary Beatra commands.

Mitigation: Disable automatic updates with python3 scripts/mcp_client.py update --auto off when silent updates are not acceptable, and use update --check to inspect the available version.

Risk: Billable video generation can be duplicated if a paid request is retried with changed arguments or a new request identity after transport uncertainty.

Mitigation: Use one opaque client_request_id per logical request, poll existing tasks before replay, and retry only byte-identical arguments with the same request identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/office-floor-tour)
- [Beatra skill homepage](https://beatra.ai/skills/office-floor-tour)
- [Office floor tour workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown with JSON and shell command snippets; video outputs are returned as Beatra task artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one floor walkthrough clip per labeled still and reports task status, output media facts, and net charged credits when available.]

## Skill Version(s):

0.1.2 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
