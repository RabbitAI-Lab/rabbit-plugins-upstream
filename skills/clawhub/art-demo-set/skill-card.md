## Description:

Turn user-supplied drawing steps into one still per art demo page. This classroom art still studio lays out each step-by-step art demo from the supplied demo points. Use it for art demonstration stills, drawing step pages, and an art demo set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, educators, and content creators use this skill to plan and generate one classroom art demonstration still for each user-supplied drawing step. The skill helps preserve confirmed lesson text, step order, billing identity, and task recovery details while using Beatra image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared Beatra bearer token in ~/.beatra and requests broad Beatra account capabilities.

Mitigation: Review the Beatra approval page before authorizing, keep the token out of chat, logs, command arguments, environment variables, and other files, and uninstall or reconnect if the account context is wrong.

Risk: The bundled client silently updates package files by default.

Mitigation: Disable automatic updates with the documented `python3 scripts/mcp_client.py update --auto off` command before use if silent package replacement is not acceptable.

Risk: Generation calls spend Beatra credits and uncertain transport recovery can duplicate work if request identity is changed.

Mitigation: Confirm the production card before billable calls, use one opaque client_request_id per approved step, retry only identical frozen payloads with the same ID, and report billing.net_charged_credits from the task response.

## Reference(s):

- [Art-demo workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/art-demo-set)
- [Beatra skill homepage](https://beatra.ai/skills/art-demo-set)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with inline JSON and shell command examples, plus generated image artifacts returned by Beatra tasks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free labeled page plan before billable generation, then returns stills in step order with task IDs, resolved models, dimensions, formats, and billing.net_charged_credits when generation succeeds.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
