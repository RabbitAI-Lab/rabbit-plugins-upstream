## Description:

This skill helps agents operate CastingWords through an OOMOL-connected account to check balances, retrieve transcripts, view transcription status, and submit public media URLs for transcription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected CastingWords account through OOMOL, including checking balance, retrieving transcripts, checking transcription status, and submitting public media URLs for human transcription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitting a transcription sends the supplied public media URL to CastingWords and may create a billable transcription job.

Mitigation: Confirm the exact submit_transcription payload and expected effect with the user before running the write action.

Risk: Connector action schemas can change over time, which could make a stale payload invalid or misleading.

Mitigation: Inspect the live action schema with oo connector schema before constructing and running each connector payload.

## Reference(s):

- [CastingWords homepage](https://castingwords.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-castingwords)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Text, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return transcript text, HTML transcript content, balance values, status details, and connector execution metadata depending on the selected action.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
