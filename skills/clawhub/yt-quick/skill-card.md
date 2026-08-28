## Description:

Provides quick YouTube lookups for pasted links or video IDs, including transcripts, channel-latest checks, and topic search through TranscriptOut.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch YouTube transcripts, search for videos or channels, and check recent channel posts through TranscriptOut-backed API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a TranscriptOut API key and setup instructions may involve the agent handling or persisting that secret.

Mitigation: Use a scoped secret manager or runtime environment-variable mechanism, avoid pasting reusable secrets into chat, and revoke or remove the key when it is no longer needed.

Risk: The skill sends YouTube lookup requests to the external TranscriptOut API and depends on that service being reachable.

Mitigation: Install only when external TranscriptOut access is acceptable for the intended workflow, and review API responses and request IDs before relying on results.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API Key Setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/yt-quick)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON or text API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
