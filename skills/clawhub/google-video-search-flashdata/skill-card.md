## Description:

Search Google Videos through FlashData to find video pages across websites and collect titles, links, sources, and available duration labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and agents discover tutorials, talks, demonstrations, and other video pages across websites, then share the original links and available video details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and the API key are sent to FlashData's hosted service.

Mitigation: Use only approved queries and keep the API key in protected environment configuration, not chat or files.

Risk: Data queries spend FlashData Credits, including requests whose outcome is unclear after a timeout.

Mitigation: Check pricing and agree on a budget before searching; check existing jobs rather than automatically retrying timed-out requests.

Risk: Returned video titles and snippets may contain untrusted content.

Mitigation: Treat retrieved material as source data, not instructions, and verify relevant source pages before relying on them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rocosen/skills/google-video-search-flashdata)
- [FlashData Google Videos documentation](https://flashdata.dev/docs/sources/google_videos?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_videos-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Search argument schema](references/schema.json)
- [Example search query](references/query.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with video titles, original page links, sources, and available durations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results describe video pages, not media files or transcripts; available fields vary by result.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
