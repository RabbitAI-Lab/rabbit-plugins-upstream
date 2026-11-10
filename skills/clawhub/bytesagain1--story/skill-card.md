## Description:

Story is a local command-line story and content logging tool with commands for drafting, editing, optimization labels, search, status, and export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bytesagain1](https://clawhub.ai/user/bytesagain1)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams can use this skill to organize story, marketing, and copywriting entries in a local terminal workflow and export the logged data. It should be treated as a plaintext local logger rather than an autonomous editor, translator, optimizer, or scheduler.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Command names and summaries may imply AI editing, translation, optimization, or scheduling behavior that the artifact does not provide.

Mitigation: Use the skill as a local content logger and verify any creative transformations or publishing schedules through separate tools or human review.

Risk: Story and marketing entries are stored locally as plaintext and exports may include sensitive or untrusted content.

Mitigation: Avoid storing proprietary drafts unless local plaintext storage is acceptable, and review JSON, CSV, or TXT exports before sharing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bytesagain1/skills/story)
- [BytesAgain Homepage](https://bytesagain.com)

## Skill Output:

**Output Type(s):** [text, shell commands, files, configuration]

**Output Format:** [Terminal text with local JSON, CSV, or TXT export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores plaintext logs under ~/.local/share/story.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
