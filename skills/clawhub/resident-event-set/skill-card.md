## Description:

Turn user-supplied resident event names and points into a four-to-eight still resident event set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and community office staff use this skill to turn confirmed resident-event names and points into a matching set of still image prompts, approval cards, Beatra generation calls, and delivery notes. It is intended for activity still packs and resident event graphic sets where each named activity becomes one still.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for and persists a shared Beatra device token with broad media, wallet, artifact, and task permissions.

Mitigation: Authorize only accounts where Beatra credit spending and uploaded reference media are acceptable; keep the token in the local Beatra credential file and do not expose it in chat, logs, command arguments, or environment variables.

Risk: Billable image generation can spend Beatra credits, and request-time cost estimates may differ from final measured usage.

Mitigation: Require the user-facing production card before paid generation, read the live model card for current price and constraints, submit each still once with its own request identity, and report returned net charged credits.

Risk: Automatic updates are enabled by default and can replace package-owned files when a newer release is available.

Mitigation: Users who do not want silent update checks can run `python3 scripts/mcp_client.py update --auto off`; the bundled updater verifies discovery data, archive checksums, manifest data, and package-owned files before replacement.

Risk: Generated stills can contain unreadable or incorrect small text, which could misrepresent event details.

Mitigation: Review visible printed text against the confirmed pack list, report unreadable small type as a review item, and avoid presenting generated text as an official notice or attendance record.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/resident-event-set)
- [Beatra package homepage](https://beatra.ai/skills/resident-event-set)
- [Resident event pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces pack lists, approval cards, Beatra task calls, task IDs, resolved model details, billing notes, and review guidance; generated image artifacts are returned by Beatra tasks.]

## Skill Version(s):

0.1.2 (source: server release evidence and packaged script constants)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
