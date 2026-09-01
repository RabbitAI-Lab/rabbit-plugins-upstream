## Description:

Turns Xiaohongshu wealth FAQ notes into separate 2 to 15 second talking FAQ clips from advisor-supplied product answers and inspected still images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External wealth advisors and their agents use this skill to plan, approve, generate, and review short Xiaohongshu FAQ talking clips based only on public note questions and already-written product answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device credential and can contact Beatra services beyond the narrow FAQ-clip workflow.

Mitigation: Install only after accepting that account-level access model, keep the credential in the documented local credential file, and revoke or reconnect through Beatra when the installation should no longer have access.

Risk: The workflow can spend Beatra credits for lookup, voice clone, speech, and video tasks.

Mitigation: Require the skill's separate approval card for each paid stage, quote live prices, use one opaque client request identity per task, and report net charged credits from terminal task results.

Risk: Selected local stills, voice samples, or audio may be uploaded to Beatra services for generation.

Mitigation: Inspect each asset first, confirm likeness and voice rights, upload only selected files through the bundled client, and avoid passing local paths directly to generation tools.

Risk: Silent automatic updates are enabled by default.

Mitigation: Use the documented update controls to disable automatic checks or run manual update checks when stricter change control is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/xiaohongshu-wealth-faq-talking)
- [Beatra skill homepage](https://beatra.ai/skills/xiaohongshu-wealth-faq-talking)
- [Wealth FAQ talking-clip workflow](references/workflow.md)
- [Xiaohongshu wealth FAQ note lookup](references/note-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown approval cards, JSON tool payloads, shell commands, and generated media artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces separate 2 to 15 second clips; reports returned MIME type, duration, size, task status, and net charged credits when available.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
