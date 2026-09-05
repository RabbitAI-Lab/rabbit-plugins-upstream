## Description:

詹明明·口播剪辑 helps an agent turn talking-head footage into a publishable edit plan or ChatCut timeline by restructuring spoken content, cleaning speech, applying fixed pacing and caption defaults, and preserving the speaker's actual words.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents use this skill after filming talking-head footage to plan or execute a structured edit: remove unusable or repeated material, preserve the speaker's wording, apply account-specific pacing and caption defaults, and prepare a deliverable timeline or export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may activate the workflow when the user only intended a general editing request.

Mitigation: Confirm the target project, assets, and requested edit scope before changing a timeline or writing related notes.

Risk: Timeline edits can remove or reorder spoken material in ways the creator did not intend.

Mitigation: Use the skill's step-by-step checkpoints, read back the refreshed timeline after each major edit, and require user confirmation before moving to dependent stages.

Risk: B-roll or source images may expose faces, payment data, customer details, or other sensitive visual information.

Mitigation: Apply masking or exclusion rules before public use, inspect full-size frames rather than thumbnails, and keep separate backups before approving original-image cleanup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-cut)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [ChatCut 实操](artifact/references/ChatCut实操.md)
- [内容层重组](artifact/references/内容层重组.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional tool commands, edit checkpoints, and review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce timecoded edit decisions, caption/highlight candidates, ChatCut workflow steps, and final verification guidance.]

## Skill Version(s):

0.2.4 (source: server release evidence; artifact frontmatter says 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
