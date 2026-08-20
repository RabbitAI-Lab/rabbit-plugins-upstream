## Description:

Creates podcast chapters, highlights, and show notes from podcast audio or transcripts, with multilingual and formatted output support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and content teams use this skill to turn podcast audio or transcripts into chapters, highlights, show notes, and structured publishing outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the skill as suspicious because it requests command execution and file write access with broad operating instructions.

Mitigation: Install only in a sandbox or constrained workspace, review any command before approval, and grant access only to the podcast files needed for the task.

Risk: Podcast media and transcripts may contain private, copyrighted, or otherwise sensitive content.

Mitigation: Use non-sensitive inputs, confirm rights to process the media, and avoid exposing credentials, private transcripts, or unrelated project files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thcjp/skills/podcast-chaptering-2)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown, text, JSON, and file-oriented outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write local media or transcript files and may propose command execution depending on agent permissions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
