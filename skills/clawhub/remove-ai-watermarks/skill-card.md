## Description:

Helps inspect and remove AI watermarks and provenance marks from images and video the user owns or is authorized to edit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can inspect their own images or videos for AI provenance marks and, where authorized, remove selected visible marks, invisible marks, or embedded metadata.

### Deployment Geography for Use:

Global, subject to local restrictions on removing AI labels, including in mainland China.

## Known Risks and Mitigations:

Risk: Removal could affect someone else's protected content or enable misleading claims about origin.

Mitigation: Use only on content the user owns or is authorized to edit; do not remove third-party commercial watermarks or claim the result is human-made.

Risk: Installations or removal commands may change local files or require substantial dependencies.

Mitigation: Review proposed installs, write to a separate output unless overwrite is explicitly requested, and check that an output file exists before reporting success.

Risk: A missing local provenance signal can be mistaken for proof that a file is clean or human-made.

Mitigation: Report uncertain inspection results as unknown and avoid treating removal as proof of origin.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Project repository (listed in metadata)](https://github.com/wiltodelta/remove-ai-watermarks)
- [Project homepage](https://raiw.cc)
- [Command recipes](artifact/references/commands.md)
- [Install guidance](artifact/references/install.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and inspection results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce edited image or video files when removal is requested and supported.]

## Skill Version(s):

1.0.11 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
