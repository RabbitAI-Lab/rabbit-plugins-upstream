## Description:

Turns a product and confirmed facts into a WeChat Channels short-video script with a second-by-second segment table, full spoken narration, placed product-link conversion beats, and a six-dimension draft score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and store operators use this skill to draft WeChat Channels selling videos from supplied product facts. It produces the fact sheet, timed segment table, full narration, product-link beats, and draft score, with optional storyboard frames or voiced narration after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device authorization can spend credits, read and manage tasks, and access broader media-generation capabilities than the script workflow normally needs.

Mitigation: Install only in an account and environment where that authority is acceptable, review Beatra account activity, and reconnect or revoke shared credentials when appropriate.

Risk: Automatic updates can silently replace package files.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when silent package replacement is not acceptable, and review updates before re-enabling them.

## Reference(s):

- [Structuring the script](references/script-structure.md)
- [Placing the product-link beats](references/product-link-beats.md)
- [Script studio workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wechat-channels-script-studio)
- [Beatra skill homepage](https://beatra.ai/skills/wechat-channels-script-studio)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, narration prose, approval prompts, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional storyboard frames and voiced narration are requested only after approval and return Beatra task and artifact metadata.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
