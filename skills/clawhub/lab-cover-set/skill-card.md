## Description:

Turn user-supplied assignment names and points into a four-to-eight still lab cover set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan and generate a coordinated set of lab report or assignment cover stills from assignment names and point values they already supplied.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra device-token scopes, including wallet spending and media, task, and artifact access.

Mitigation: Install only for users who accept those scopes, keep the token out of chat, logs, command arguments, and diffs, and disconnect or uninstall when access is no longer needed.

Risk: Billable image generation can create charges or duplicate work if a request is retried with changed inputs.

Mitigation: Require the itemized approval card before paid calls, use one opaque client_request_id per still, and retry only byte-identical uncertain requests.

Risk: Silent package updates are enabled by default.

Mitigation: Review the automatic update behavior before installation and disable silent checks with the documented update command when that is not acceptable.

Risk: Optional local uploads and generated prompts may include sensitive assignment or reference material.

Mitigation: Provide only files and text needed for the cover set, and avoid exposing private prompts, tokens, or sensitive input content during recovery or reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/lab-cover-set)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Lab cover pack workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and JSON snippets; generated cover stills are delivered through Beatra tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans one still per supplied assignment, normally four to eight stills, with one paid generation call per still.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
