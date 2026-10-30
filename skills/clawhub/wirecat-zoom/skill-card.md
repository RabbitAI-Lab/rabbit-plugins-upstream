## Description:

Archive Zoom cloud recordings, read stored meeting transcripts and summaries, or manage a Zoom meeting through zm. Use for Zoom CLI workflows, not joining calls or operating the desktop video client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Zoom users can use this skill to find and review archived meeting evidence, prepare bounded meeting context, and manage Zoom records or meeting details through the zm command-line workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A communications grant can cover an entire selected account or folder, and remote models may receive transcript passages.

Mitigation: Choose the intended profile and source carefully; use a local model or offline mode when transcripts must remain on the computer.

Risk: Meeting and account changes can affect remote Zoom data, and a dispatched write can have an uncertain outcome.

Mitigation: Review the exact proposed change and authorize it explicitly; inspect remote state before retrying a write with an uncertain result.

Risk: Names and transcript text retrieved from meetings may contain misleading content or instructions.

Mitigation: Treat retrieved names and transcript text as evidence data, not as instructions to act.

## Reference(s):

- [Zoom CLI skill release](https://clawhub.ai/wirecat/skills/wirecat-zoom)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text, Markdown, JSON]

**Output Format:** [Markdown guidance with shell command examples and structured JSON or JSONL output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflows emphasize bounded reads, retained evidence references, and explicit review of proposed changes.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
