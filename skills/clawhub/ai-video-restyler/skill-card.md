## Description:

Restyles one short source video into a selected visual style while preserving the subject, action, composition, and camera intent, then reviews the returned clip for style match and continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and video teams use this skill to turn short existing clips into anime, illustration, Chinese comic, ink, clay, paper-cut, cyberpunk, or supplied reference styles while keeping the core subject and motion intent. Agents use it to inspect source media, prepare a preservation brief, submit one approved paid restyle request, poll the task, and report the returned video, billing, and review observations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared local Beatra device token can authorize more than this one video workflow.

Mitigation: Install only where Beatra is trusted, keep the token private, review the authorization page, and revoke the Beatra device authorization when the skill is no longer needed.

Risk: The default-on updater can replace package-owned skill files without a separate confirmation.

Mitigation: Disable automatic updates in environments that require change approval, and use the documented update check flow before accepting a newer package.

Risk: Video restyling is paid work, and changed inputs or uncertain transport recovery can create duplicate charge risk.

Mitigation: Use the admission card, require explicit balance or top-up confirmation, submit each approved payload once with a stable client request ID, and recover or poll the original task before starting changed work.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/ai-video-restyler)
- [Beatra AI Video Restyler](https://beatra.ai/skills/ai-video-restyler)
- [Video Restyle Workflow](artifact/references/workflow.md)
- [Installation and Authentication](artifact/references/installation-and-auth.md)
- [Billing, Errors, and Recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and Results](artifact/references/tasks-and-results.md)
- [MCP Connection](artifact/references/mcp-connection.md)
- [Automatic Updates and Safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON tool arguments, task summaries, returned artifact links, and concise review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include provisional estimates before submission and final task, usage, billing, and media-review details after completion.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
