## Description:

Reach for this whenever what was SAID in a YouTube video matters: a pasted link or bare video ID, a summary, quote, translation or fact-check request, notes from a lecture, or research that leans on a specific video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to fetch YouTube transcripts for summaries, quotes, translations, fact-checking, lecture notes, and research grounded in a specific video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can require the agent to handle account signup, one-time passcodes, API keys, and persistent secret storage.

Mitigation: Create the TranscriptOut account and API key yourself when possible, then store TRANSCRIPTOUT_API_KEY in the platform's protected secret store instead of pasting it into chat or saving it in shell profile files.

Risk: Transcript requests contact TranscriptOut and consume account credits.

Mitigation: Use the skill only when transcript content is needed, prefer format=text for reasoning tasks, and avoid bulk transcript pulls for videos the user has not selected.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API key setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/transcript)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API responses that may be plain text, JSON, SRT, VTT, or SRV3 transcript data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
