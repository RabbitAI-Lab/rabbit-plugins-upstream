## Description:

CastingWords (castingwords.com). Use this skill for ANY CastingWords request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate CastingWords through an OOMOL-connected account, including balance checks, transcript retrieval, transcription status lookups, and public media URL transcription submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Review installation instructions first, prefer a verified release or package manager, and do not allow an agent to automatically run the remote installer.

Risk: Submitting a transcription sends a publicly accessible audio or video URL for paid asynchronous processing.

Mitigation: Confirm the exact submission payload and intended effect with the user before running the write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-castingwords)
- [CastingWords Homepage](https://castingwords.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data when executed through the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
