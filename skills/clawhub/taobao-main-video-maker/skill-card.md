## Description:

Create a Taobao product main-image video or Tmall product main-image video from product photos, selling points, and brand references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and operators use this skill to turn product photos, selling points, and brand references into concise Taobao or Tmall main-image product video workflows. It helps an agent plan the product story, confirm paid Beatra stages, submit approved generation requests, poll tasks, and report the resulting video artifact and billing facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token can access more than this one video workflow and billable operations may spend credits.

Mitigation: Use a dedicated Beatra account or limited balance, and review each paid confirmation before allowing generation work.

Risk: The package silently checks for and installs newer releases by default.

Mitigation: Disable automatic updates after install when tighter change control is required, and review update status before sensitive work.

## Reference(s):

- [ClawHub Skill Release Page](https://clawhub.ai/beatra-ai/skills/taobao-main-video-maker)
- [Beatra Skill Homepage](https://beatra.ai/skills/taobao-main-video-maker)
- [Taobao Main Product Video Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Tasks and Results](references/tasks-and-results.md)
- [MCP Connection](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON tool arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may report Beatra task IDs, returned artifact links, model details, dimensions, duration, and billing facts after approved generation work.]

## Skill Version(s):

0.1.5 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
