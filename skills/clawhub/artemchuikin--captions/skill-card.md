## Description:

Captions retrieves timestamped closed captions from public YouTube videos via TranscriptOut for reading, quoting, translating, accessibility, content review, language practice, or SRT/VTT export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve YouTube caption text for reading, quoting, translating, accessibility support, content review, language practice, or export as SRT/VTT.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TranscriptOut receives the YouTube video URLs or IDs requested through the skill.

Mitigation: Use the skill only when sharing those video identifiers with TranscriptOut is acceptable.

Risk: The setup flow can give the agent responsibility for account creation, API-key handling, and persistent secret storage.

Mitigation: Prefer creating the account and key yourself in the browser, store the key in a dedicated secret manager, and rotate or revoke it if exposure is suspected.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API key setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/captions)

## Skill Output:

**Output Type(s):** [Text, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with curl commands; retrieved captions may be JSON, plain text, SRT, VTT, or SRV3.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
