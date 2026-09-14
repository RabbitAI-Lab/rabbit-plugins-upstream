## Description:

Turn written product answers and public note questions into one spoken wealth FAQ clip per question.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External wealth advisors use this skill to turn supplied product answers and public or pasted Xiaohongshu note questions into separate short talking FAQ clips. The workflow supports note lookup, speech generation, optional voice cloning, image-to-video animation, task polling, billing reporting, and recovery while avoiding invented returns or personalized buy-or-sell advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid Beatra generation calls can spend account credits after approval cards.

Mitigation: Require stage-specific approval cards, quote live pricing before each paid lookup, clone, speech, or video stage, and report billing.net_charged_credits from terminal task results.

Risk: The skill stores a broad shared Beatra Device Token in ~/.beatra/credentials.json.

Mitigation: Keep the token only in the documented credential file with user-only permissions, never place it in commands or conversation, and rerun authorization only when recovery or reconnection is required.

Risk: The bundled client silently checks for and applies package updates by default.

Mitigation: Use the documented update controls to disable automatic checks when desired and rely on the packaged checksum and rollback protections for accepted updates.

Risk: Generated wealth FAQ clips could misstate product information or imply financial advice.

Mitigation: Use only advisor-supplied product facts, do not invent returns or personalized buy-or-sell lines, and review each clip against the approved product line before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/xiaohongshu-wealth-faq-talking)
- [Beatra skill homepage](https://beatra.ai/skills/xiaohongshu-wealth-faq-talking)
- [Wealth FAQ talking workflow](references/workflow.md)
- [Wealth FAQ note lookup](references/note-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with approval cards, JSON payload examples, shell commands, task summaries, and generated media artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one short FAQ clip per approved slot and reports returned artifact details, task status, usage, and net charged credits when present.]

## Skill Version(s):

0.1.3 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
