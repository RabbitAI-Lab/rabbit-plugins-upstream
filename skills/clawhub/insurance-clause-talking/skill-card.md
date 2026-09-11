## Description:

Turns user-supplied insurance policy clauses and authorized stills into short talking clips, one clip per still, using only clause explanation lines grounded in the supplied text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External insurance advisors and wealth educators use this skill to turn supplied policy clauses and authorized stills into short, clause-grounded talking clips for explanation packs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra account connection can spend credits and upload selected files.

Mitigation: Confirm each paid clone, speech, and video stage before submission, review account activity, and avoid sensitive insurance documents or images unless sending them to Beatra is acceptable.

Risk: The package stores a shared local bearer credential for Beatra access.

Mitigation: Keep the credential only in the documented private credential file and never expose tokens in chat, logs, command arguments, environment variables, or copied files.

Risk: Automatic self-updates are enabled by default.

Mitigation: Disable silent update checks with the documented update command when automatic package replacement is not desired.

Risk: The package reports installation and platform registration data.

Mitigation: Install only when this telemetry is acceptable for the deployment context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/insurance-clause-talking)
- [Beatra skill homepage](https://beatra.ai/skills/insurance-clause-talking)
- [Clause talking-clip workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with JSON payload examples and shell command blocks; remote tasks can return generated media files and artifact metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one talking-clip task per approved still or segment; paid clone, speech, and video stages require explicit current cost confirmation.]

## Skill Version(s):

0.1.3 (source: server release evidence and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
