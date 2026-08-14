## Description:

Drafts X posts on a weighted content schedule, sends drafts to the authorized user for approval, publishes only approved packages, and supports reply drafting, photo ingestion, and content maintenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[soos3d](https://clawhub.ai/user/soos3d)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and individual creators use this skill to draft, approve, and publish posts for their own X account while maintaining backlog notes, voice guidance, metrics, and a photo library. It is intended for controlled account automation where publishing is gated by an authorized user's explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A misconfigured approval recipient could allow the wrong Telegram user to approve drafts or ingest photos.

Mitigation: Configure telegramTo carefully and review settings.json before enabling publishing or photo ingestion.

Risk: Selected user notes may be stored locally for future drafting and could include sensitive project or personal details.

Mitigation: Do not send secrets or private personal details as project notes, and periodically review local backlog and state files.

Risk: Publishing relies on configured X authentication and can affect a real social account.

Mitigation: Review X authentication setup, local pillar files, and publishing mode before enabling live publishing; keep approval gates enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/soos3d/skills/postflight)
- [Skill definition](artifact/SKILL.md)
- [Drafting and approval](artifact/DRAFTING.md)
- [Publishing via the X API](artifact/PUBLISH-API.md)
- [Publishing via browser](artifact/PUBLISH-BROWSER.md)
- [Reply drafting](artifact/REPLY-DRAFTING.md)
- [Photo ingestion](artifact/PHOTO-INGESTION.md)
- [Content sourcing](artifact/CONTENT.md)
- [Voice guidance](artifact/VOICE.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline shell commands, configuration snippets, and approval messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local postflight-state files, draft social posts, prepare approval packages, ingest photo-library entries, and execute configured X publishing steps after approval.]

## Skill Version(s):

1.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
