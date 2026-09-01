## Description:

Paste a short-video link, file, screenshots, transcript, or description to break a proven reference into hook, beats, and call to action, then rebuild that structure around a new subject as a shot list, generated frames, narration, and a vertical clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content teams use this skill to study a performing short video and adapt its structure to their own product, service, topic, or account. It is suited to benchmark remakes for TikTok, Reels, Shorts, WeChat Channels, Douyin, Xiaohongshu, Instagram, YouTube, and X workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra credential with paid media-generation authority.

Mitigation: Review the Beatra approval scopes before installation, keep the credential private, and approve paid lookup, frame, narration, and video calls only when the quoted scope and estimate match the intended work.

Risk: The bundled client silently checks for and applies package updates by default.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` before use if automatic package updates are not acceptable for the environment.

Risk: The workflow can upload local files as reference inputs.

Mitigation: Only provide files intentionally selected for the remake and avoid uploading local files that contain private, sensitive, or unrelated content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/viral-video-teardown-remake)
- [Beatra skill homepage](https://beatra.ai/skills/viral-video-teardown-remake)
- [Reading the reference from a link](references/reference-lookup.md)
- [Reading the reference](references/teardown.md)
- [Rewriting onto your subject](references/remake-plan.md)
- [Remake workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Media assets]

**Output Format:** [Markdown teardown and shot-list tables, shell-command examples, configuration guidance, generated media artifact links, and task/billing summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to a 9:16 vertical remake, separates on-screen visuals from spoken narration, and requires explicit approval before paid lookup, frame, narration, and video calls.]

## Skill Version(s):

0.1.9 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
