## Description:

Creates a short narrated vertical recommendation video from a topic, including a script, beat frames, narration, optional music, and an opening-frame animation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to turn a product, service, or topic into a concise spoken recommendation short. It guides the agent through pattern selection, shot-list approval, paid Beatra generation calls, media review, and final delivery of returned task facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client stores a shared Beatra Device Token under ~/.beatra.

Mitigation: Use the authorization helper only in a trusted local environment, keep ~/.beatra private, never expose the token in chat or command arguments, and revoke the connection from the Beatra Console when access should end.

Risk: The bundled client sends package and platform installation metadata to Beatra.

Mitigation: Install only if this telemetry is acceptable for the deployment context, and review the security summary before enabling the skill.

Risk: Automatic package updates are enabled silently by default.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` to require manual update control, or `python3 scripts/mcp_client.py update --check` to inspect the available version without replacing files.

Risk: The workflow can make paid Beatra generation calls after user approval.

Mitigation: Keep the documented approval gates: approve the shot list before preparation calls, review generated materials before the video call, and retry uncertain paid calls only with the same frozen request identity.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/oral-seeding-video-maker)
- [Beatra Skill Homepage](https://beatra.ai/skills/oral-seeding-video-maker)
- [Choosing the Pattern](references/script-patterns.md)
- [Writing Spoken Lines](references/spoken-lines.md)
- [Seeding Video Workflow](references/workflow.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and shell command snippets plus returned artifact links and task facts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected pattern, approved shot list, still-frame links, narration or music artifact links, final video link, task IDs, resolved models, durations, dimensions, and billing facts returned by Beatra.]

## Skill Version(s):

0.1.5 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
