## Description:

Turn already-written short sleep stories into one spoken clip per labeled story.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External producers use this skill to turn pre-written short sleep stories into labeled spoken clips, including optional catalog voices or consented cloned voices. The skill guides planning, authorization, Beatra speech generation, billing checks, task polling, and recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests broad Beatra media-generation, wallet, task, artifact, and voice permissions for a narrow sleep-story workflow.

Mitigation: Install only when the user accepts shared full-scope Beatra authority, and reconnect or revoke access if that permission scope is not appropriate.

Risk: The package uses a persistent local Beatra device token.

Mitigation: Use it only in a trusted user environment, keep the credential file private, and use the documented uninstall or disconnect flow when access is no longer needed.

Risk: Voice cloning can involve local sample uploads and likeness rights.

Mitigation: Upload only inspected, authorized samples and require explicit voice rights before any clone request.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable automatic updates or run manual update checks when silent package replacement is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/sleep-story-voice)
- [Beatra skill homepage](https://beatra.ai/skills/sleep-story-voice)
- [Sleep story workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include labeled listen lists, Beatra task IDs, audio metadata, net charged credits, and recovery guidance after remote task completion.]

## Skill Version(s):

0.1.1 (source: server release evidence and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
