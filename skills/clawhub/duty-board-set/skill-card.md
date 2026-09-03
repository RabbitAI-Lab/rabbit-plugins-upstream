## Description:

Turn user-supplied classroom duty roster slots and duty lines into a four-to-eight still duty board set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External educators and classroom staff use this skill to plan and generate matching duty-board still image packs from roster slot names and approved duty lines they provide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests broad Beatra device authorization and uses a shared local credential.

Mitigation: Install only in trusted agent environments, protect the local Beatra credential files, and revoke or reconnect access when account control changes.

Risk: Roster content and first-use registration metadata are sent to Beatra services.

Mitigation: Provide only approved duty slot names and duty lines, avoid unnecessary student or school identifiers, and review suitability for school or managed environments before use.

Risk: Silent package updates are enabled by default.

Mitigation: Use the documented update controls to disable automatic checks when managed change control is required, and run explicit update checks before sensitive work.

Risk: Image generation is billable and failed recovery can create duplicate work if request identity changes.

Mitigation: Confirm the production card before paid calls, keep one opaque client request ID per still, and retry uncertain submissions only with identical arguments.

## Reference(s):

- [Duty board pack workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/duty-board-set)
- [Beatra skill homepage](https://beatra.ai/skills/duty-board-set)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell and JSON examples, plus generated image artifacts returned by Beatra tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One still per confirmed duty slot, normally four to eight stills, with one paid generation task per still.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
