## Description:

Create a coordinated REDnote (Xiaohongshu) OOTD lookbook from outfit photos or a styling idea, including a vertical 3:4 image carousel, title ideas, caption angles, tags, and optional paid Xiaohongshu lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, fashion marketers, and agent users use this skill to turn an outfit photo or styling idea into a coordinated Xiaohongshu OOTD lookbook and ready-to-publish post package. It can also perform separately approved, paid Xiaohongshu lookup to ground the post in current platform examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account permissions.

Mitigation: Review the requested account and device access before installation, and manage Beatra account access in the Beatra Console.

Risk: Selected outfit files may be uploaded for remote processing.

Mitigation: Use only outfit files the user is comfortable sending to the remote service, and avoid uploading sensitive or unrelated media.

Risk: The packaged client silently checks for and applies verified automatic updates by default.

Mitigation: Consider disabling automatic updates with the documented update --auto off command and review the update safety documentation before use.

Risk: Optional Xiaohongshu lookup and image generation can consume paid Beatra credits.

Mitigation: Confirm each paid lookup or generation request separately, quote the current maximum charge before execution, and preserve request IDs to avoid duplicate paid work.

## Reference(s):

- [Zhongcao OOTD Lookbook Maker listing](https://clawhub.ai/beatra-ai/skills/zhongcao-ootd-lookbook-maker)
- [Beatra skill homepage](https://beatra.ai/skills/zhongcao-ootd-lookbook-maker)
- [Lookbook planning](references/lookbook-planning.md)
- [REDnote OOTD Lookbook workflow](references/workflow.md)
- [Reading Xiaohongshu](references/note-lookup.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples, shell commands, generated image artifact links, and post copy]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an ordered lookbook plan, paid execution confirmations, task and billing facts, title ideas, caption beats, tags, and risk-aware recovery guidance.]

## Skill Version(s):

0.1.4 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
