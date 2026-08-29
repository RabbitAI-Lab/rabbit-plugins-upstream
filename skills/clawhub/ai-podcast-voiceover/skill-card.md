## Description:

Turn an article, notes, or a finished script into a listener-ready solo podcast episode with a consistent host voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editorial teams, and agent users use this skill to adapt supplied articles, notes, outlines, or finished scripts into single-host podcast scripts and MP3 narration while preserving a recurring host voice, pronunciation guidance, and delivery records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses shared Beatra device authorization stored under ~/.beatra.

Mitigation: Install only after accepting the shared authorization model, keep the token out of prompts and logs, and use the documented uninstall or Beatra Console revocation path when access should end.

Risk: The bundled client performs silent package-owned self-updates by default.

Mitigation: Use the documented `python3 scripts/mcp_client.py update --auto off` command when explicit control over code changes is required; the updater verifies package identity, checksums, and owned paths before replacement.

Risk: Speech synthesis and optional music generation are paid asynchronous Beatra tasks.

Mitigation: Review each production card before approval, keep speech and music approvals separate, use one stable client_request_id per logical paid request, and recover uncertain submissions only with unchanged arguments.

Risk: A solo TTS episode may be mistaken for a mixed, multi-host, mastered, or published podcast episode.

Mitigation: Use this skill for single-host episode audio, route multi-host or assembled productions elsewhere, and deliver returned artifacts with their actual task, usage, billing, and media facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ai-podcast-voiceover)
- [Beatra AI Podcast Voiceover homepage](https://beatra.ai/skills/ai-podcast-voiceover)
- [Episode script guidance](references/episode-script.md)
- [Show profile](references/show-profile.md)
- [Voice, delivery, and recovery](references/voice-and-delivery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, audio artifacts]

**Output Format:** [Markdown guidance with JSON examples, shell commands, production confirmation cards, and returned MP3 artifact metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces single-host podcast scripts and narration workflow records; generated audio is returned through Beatra task artifacts rather than embedded in the text response.]

## Skill Version(s):

0.1.6 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
