## Description:

Generates printable Word (.docx) vocabulary flashcards for young children with front-side illustrations, back-side recall labels, and double-sided 2x2 mirror alignment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tiandeyu](https://clawhub.ai/user/tiandeyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, educators, parents, and developers use this skill to create print-ready English or Chinese vocabulary flashcards for preschool children. It guides agents through validating word lists, generating emoji-backed card images, and assembling double-sided Word documents for cutting and printing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Python commands and installs Python dependencies.

Mitigation: Install and run it in a dedicated project or temporary directory, and review or pin dependency versions before use.

Risk: The emoji download step contacts jsDelivr/Twemoji for artwork.

Mitigation: Run the downloader only in environments where outbound access to that source is acceptable, or pre-stage reviewed artwork assets.

Risk: Re-running the scripts overwrites generated emoji, front, back, and DOCX outputs.

Mitigation: Set EMOJI_OUT and OUT_DOCX to disposable or release-specific paths and avoid pointing them at sensitive locations.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/tiandeyu/flashcards-word)
- [ClawHub skill page](https://clawhub.ai/tiandeyu/skills/flashcards-word)
- [Word set examples](references/word-sets.md)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and Python scripts that generate PNG and DOCX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces editable .docx flashcard sheets and generated PNG card artwork when executed in a local Python environment.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
