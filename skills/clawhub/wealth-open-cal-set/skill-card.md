## Description:

Turn user-supplied open windows into a four-to-eight still wealth open calendar. This open-period calendar set studio lays out each named fund open window calendar as its own still. Use it for open window calendar stills, wealth calendar stills, and an open calendar pack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn already supplied wealth or fund open-window details into a consistent four-to-eight still calendar pack. It helps plan, confirm, generate, review, and recover each paid calendar-still task without inventing missing financial dates or product facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests a shared Beatra Device Token with spending-capable and broad media permissions.

Mitigation: Install only in a Beatra account or environment where that access is acceptable, and review the requested authorization before approving it.

Risk: The bundled client silently checks for and installs newer package releases by default.

Mitigation: Disable automatic updates after installation with `python3 scripts/mcp_client.py update --auto off` when change control or review is required.

Risk: Paid image generation can consume credits once the user approves generation.

Mitigation: Show the current model price, one paid call per window still, and the full slot list before submitting billable work; retry only unchanged requests with the same request identity.

Risk: Generated calendar stills may contain unreadable or incorrect printed lines and should not be treated as certified financial guidance.

Mitigation: Use only user-supplied open-window facts, review visible text against the confirmed pack list, and report unread small type as a review item.

## Reference(s):

- [Wealth open calendar pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Skill page](https://clawhub.ai/beatra-ai/skills/wealth-open-cal-set)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/wealth-open-cal-set)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans one still per user-supplied open window and delivers task IDs, resolved models, dimensions, formats, billing details, and review notes.]

## Skill Version(s):

0.1.1 (source: server evidence release.version and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
