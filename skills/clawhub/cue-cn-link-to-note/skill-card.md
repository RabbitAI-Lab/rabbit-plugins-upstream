## Description:

Drafts one Markdown note from a URL or local source, with source-anchored points, a located verbatim quotation, named gaps, and a source line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Readers who want to keep one traceable note use the skill to turn a single article or local text into a structured note whose key points and quotation can be checked against the source. A person decides whether the note is accurate and worth keeping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential source material may be sent to or retained by the optional external parser, whose behavior was not verified.

Mitigation: Use local processing for confidential material. Before enabling the parser, check what it sends and retains, test with synthetic content, and use a reviewed fixed installation revision.

Risk: A drafted note can contain inaccurate bullets, quotations, locations, or omissions even when the checker passes.

Mitigation: Fill the draft bullets from the source and manually verify quotations, page locations, and omissions against the original.

Risk: Writing to an existing output path can overwrite a file.

Mitigation: Choose and check the output path before generating the note.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-cn-link-to-note)
- [Cue Omni Reader setup](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Four-section Markdown note]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One source per note; 3–7 source-anchored points, at most one located verbatim quotation, named gaps, and a dated source line. A person must verify content accuracy; a checker pass alone does not establish it.]

## Skill Version(s):

0.1.5 (source: release evidence, SKILL.md frontmatter, CHANGELOG.md dated 2026-10-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
