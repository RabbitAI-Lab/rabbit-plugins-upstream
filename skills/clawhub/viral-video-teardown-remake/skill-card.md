## Description:

Turn a short video that already worked into your own version by reading a link, file, screenshots, transcript, or description; breaking it into hook, beats, call to action, and performance drivers; then rebuilding that structure around the user's product or topic as a shot list, reference frames, narration, and either a vertical clip or segmented sources with a timecoded edit list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to analyze a short-form reference video and rebuild its structure around a new subject. It is intended for competitor video analysis, short-form script planning, storyboard and narration generation, and producing either a finished vertical remake or segmented editing materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device authorization that can spend credits and access generated tasks or artifacts.

Mitigation: Review Beatra account permissions before installation, confirm each paid operation before running it, and revoke the Beatra device authorization when the skill is no longer needed.

Risk: The skill can upload selected local files to Beatra for reference reading or generation.

Mitigation: Avoid uploading sensitive files and prefer screenshots, transcripts, or user descriptions when full video upload is unnecessary.

Risk: The bundled client can call Beatra tools beyond a narrow local allowlist.

Mitigation: Use the documented workflow gates and task ledgers, preserve stable request identifiers, and review returned task facts before approving further paid work.

Risk: The installed package can silently self-update.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when a locked installation is required, and use `python3 scripts/mcp_client.py update --check` to inspect available versions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/viral-video-teardown-remake)
- [Beatra skill homepage](https://beatra.ai/skills/viral-video-teardown-remake)
- [Reading the reference from a link](references/reference-lookup.md)
- [Reading the reference](references/teardown.md)
- [Rewriting onto your subject](references/remake-plan.md)
- [Three rebuild routes](references/rebuild-routes.md)
- [Remake workflow](references/workflow.md)
- [The six red lines](references/compliance.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, tables, JSON-style payload examples, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces teardown tables, rewritten shot lists, rebuild plans, narration guidance, artifact delivery summaries, and recovery instructions.]

## Skill Version(s):

0.3.0 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
