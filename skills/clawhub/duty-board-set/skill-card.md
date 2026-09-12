## Description:

Turns user-supplied classroom duty roster slots and duty lines into a four-to-eight set of matching duty board stills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, classroom staff, and agents assisting them use this skill to turn approved duty slot names and duty lines into a consistent classroom duty board pack. The skill guides planning, approval, paid Beatra image generation, review, delivery, and recovery for one still per named duty slot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad persistent Beatra access beyond the narrow classroom duty-board task.

Mitigation: Install only in environments that trust Beatra's credential storage and shared MCP access model; review authorization scope before managed deployment.

Risk: The bundled client silently updates package files by default.

Mitigation: Use the documented update controls to disable automatic updates where change control is required, and review package updates before use.

Risk: Approved generation calls may spend Beatra credits.

Mitigation: Require the documented production card approval before paid calls, use one opaque request ID per still, and report returned net charged credits.

Risk: Optional reference uploads can expose selected local files to Beatra.

Mitigation: Upload only user-approved reference files needed for the board pack and avoid exposing credentials, private prompts, or sensitive input content in chat or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/duty-board-set)
- [Beatra skill homepage](https://beatra.ai/skills/duty-board-set)
- [Duty board pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payload examples, task artifact references, and billing details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Beatra task IDs and image artifact references after user-approved paid generation.]

## Skill Version(s):

0.1.2 (source: evidence.release.version and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
