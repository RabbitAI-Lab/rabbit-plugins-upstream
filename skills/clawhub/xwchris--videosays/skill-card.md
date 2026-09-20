## Description:

Videosays helps agents submit video links or share text to retrieve transcript text, subtitles, transcription status, credit balance, and history through the Videosays CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xwchris](https://clawhub.ai/user/xwchris)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to transcribe one or more video links, generate subtitles, check credit balance, and inspect transcription history with Videosays.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags repeated use of an unpinned npm CLI that may execute newly changed third-party code while handling credentials and private video links.

Mitigation: Review before installing, pin the Videosays CLI to a reviewed exact version, and run it in a constrained environment.

Risk: The skill sends configured API credentials and submitted video links or share text to Videosays.

Mitigation: Use this skill only when the user trusts Videosays with the submitted content and credentials; never print or reveal API keys.

Risk: Batch transcription uses temporary files that can contain video links or share text.

Mitigation: Use secure temporary files and delete them after batch submission.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xwchris/skills/videosays)
- [Videosays Website](https://videosays.com/?utm_source=videosays_skill&utm_medium=agent_skill&utm_campaign=videosays_agent_skill)
- [Videosays API Docs](https://videosays.com/docs?utm_source=videosays_skill&utm_medium=agent_skill&utm_campaign=videosays_agent_skill&utm_content=api_docs)
- [videosays npm Package](https://www.npmjs.com/package/videosays)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI stdout containing transcript text, task status, batch status, or subtitle formats such as SRT and VTT]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include timeline transcripts, SRT, VTT, pending task receipts, batch IDs, balance/history results, and stable error guidance.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
