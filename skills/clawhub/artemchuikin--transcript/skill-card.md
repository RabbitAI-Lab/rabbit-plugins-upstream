## Description:

Fetches YouTube video transcripts through TranscriptOut for summaries, quotes, translations, fact-checking, lecture notes, and research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external users use this skill when an agent needs the spoken content of a YouTube video for analysis, citation, summarization, translation, or note-taking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires TranscriptOut authentication and may ask an agent to help create or persist an API key.

Mitigation: Create the account and API key yourself when possible, provide the key through a secure secret mechanism, and revoke it if it was pasted into chat or stored too broadly.

Risk: YouTube video IDs or URLs are sent to TranscriptOut when fetching transcripts.

Mitigation: Use the skill only for videos whose identifiers you are comfortable sending to TranscriptOut.

Risk: Transcript fetches consume credits and broad transcript pulls can quickly spend the balance.

Mitigation: Fetch transcripts only for videos the user actually asked to analyze and prefer text output unless timestamps or raw caption formats are needed.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API key setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/transcript)

## Skill Output:

**Output Type(s):** [API Calls, Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text, JSON, SRT, VTT, SRV3, or Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include transcript segments, timestamps, available caption languages, video metadata, request identifiers, and credit-balance headers depending on requested format.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
