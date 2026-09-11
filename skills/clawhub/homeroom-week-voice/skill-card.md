## Description:

Turn a written homeroom week plan into one homeroom week voice clip per labeled cue. This weekly class voice studio records each week plan voice and class notice audio from the plan the teacher already wrote, then delivers 8 to 20 homeroom voice pack files. Use it for homeroom weekly voice packs that keep one arrangement on each clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and school staff use this skill to turn an already written homeroom week plan into labeled, forwardable voice clips for class notices. It helps plan, approve, submit, recover, and deliver 8 to 20 speech clips while preserving the written plan and pronunciation constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device credential with broad media, artifact, task, and spending authority.

Mitigation: Install only on a trusted single-user device, review Beatra account permissions before authorizing, and use Beatra console revocation controls when access is no longer needed.

Risk: Billable voice clone and speech requests can spend Beatra credits.

Mitigation: Require a visible approval card before paid clone or speech work, use one opaque request identity per paid request, and check live balance or ledger data when the user asks.

Risk: Automatic package updates are enabled by default and can replace package-owned files without a separate prompt.

Mitigation: Use the documented auto-update controls to disable silent checks when review before update is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/homeroom-week-voice)
- [Beatra Skill Homepage](https://beatra.ai/skills/homeroom-week-voice)
- [Homeroom Week Voice Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client Diagnostics](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON payload examples, shell commands, and generated audio artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a visible slot list before paid work and can deliver 8 to 20 MP3 voice clips through Beatra tasks.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
