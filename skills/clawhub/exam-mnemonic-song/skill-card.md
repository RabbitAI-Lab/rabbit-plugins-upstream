## Description:

Turn one exam knowledge point into a mnemonic song you can replay, then turn the rest of the syllabus into a set. This exam mnemonic song studio writes a knowledge-point song and exam memory song from the facts you already have. Use it for bar-exam mnemonics, teacher-certification songs, accounting-exam memory songs, and other exam mnemonic playlists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Training schools, exam coaches, and candidates use this skill to turn supplied exam facts into a labeled mnemonic lyric sheet, then into one reviewed exam memory song at a time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra device authorization that can spend wallet credits and access multiple media and task capabilities.

Mitigation: Install only when that scope is acceptable, protect the local Device Token, and use Beatra account or device revocation controls when access should end.

Risk: The bundled client can silently install verified package updates from Beatra's CDN.

Mitigation: Review the automatic update behavior before deployment and disable auto-updates with the documented command when the environment requires manual update approval.

Risk: Paid music generation can consume credits or duplicate work if task recovery is handled incorrectly.

Mitigation: Use one opaque client request ID per approved generation, retry only byte-identical uncertain submissions, and report terminal usage and billing fields from the task result.

## Reference(s):

- [Exam mnemonic workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/exam-mnemonic-song)
- [Beatra skill homepage](https://beatra.ai/skills/exam-mnemonic-song)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, guidance, audio artifacts]

**Output Format:** [Markdown guidance with command examples, JSON request payloads, task status, billing details, and generated audio artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-supplied exam facts and explicit approval before each paid music generation call.]

## Skill Version(s):

0.1.1 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
