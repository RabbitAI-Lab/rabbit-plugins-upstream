## Description:

Reach for this when a video needs to become text: a pasted YouTube link or ID, a transcribe/summarize/translate request, mining a video for facts, or a bare URL shared with 'what does this say?'. Skip it for uploads and account chores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to fetch YouTube video transcripts through TranscriptOut for summarization, translation, citation, retrieval, or fact extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send YouTube video identifiers to TranscriptOut when fetching transcripts.

Mitigation: Use the skill only for videos you are comfortable disclosing to TranscriptOut.

Risk: The setup flow can involve agent-assisted account signup, OTP verification, API-key handling, and persistent credential storage.

Mitigation: Create and revoke keys yourself where possible, store the key in an approved secret manager, and avoid shell-profile persistence unless you understand its scope.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut Authentication Setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can request transcript output as text, JSON, SRT, VTT, or SRV3 through the TranscriptOut API.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
