## Description:

Turn couple-supplied ceremony facts into three wedding opening film storyboard keyframes, then one opening film.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External photo studios, wedding planners, and agents supporting couples use this skill to plan three labeled 16:9 storyboard keyframes from confirmed ceremony facts, generate those paid stills through Beatra, and then produce one 2-15 second wedding opening film after the stills are accepted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra Device Token with capabilities broader than wedding-film generation.

Mitigation: Review the Beatra approval page before authorizing, keep the token only in the documented local credential file, and revoke or uninstall the connection when it is no longer needed.

Risk: Silent automatic updates are enabled by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` before normal use if silent replacement is not acceptable, or use `python3 scripts/mcp_client.py update --check` to inspect availability first.

Risk: Recurring registration metadata is sent for the package installation.

Mitigation: Treat package slug, version, platform, and stable installation reference registration as part of the Beatra connection posture before installing.

Risk: Ceremony details and optional media references may be sent to Beatra for paid generation.

Mitigation: Provide only confirmed facts needed for the storyboard or film, avoid unnecessary sensitive details, and do not place user content or credentials in command arguments.

Risk: Network uncertainty around paid generation could cause duplicate work if requests are replayed incorrectly.

Mitigation: Use one opaque `client_request_id` per unchanged billable request, recover lost responses through task lookup, and create a new request identity only when generation inputs change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wedding-opening-film)
- [Beatra skill homepage](https://beatra.ai/skills/wedding-opening-film)
- [Wedding opening workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples, plus generated image and video task summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces three 16:9 2K storyboard stills before one 2-15 second clip; billable generation requires user approval and Beatra task polling.]

## Skill Version(s):

0.1.2 (source: evidence.release.version and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
