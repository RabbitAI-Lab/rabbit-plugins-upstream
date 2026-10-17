## Description:

Image Editor guides agents through PIL-based image edits such as text replacement, element removal, and drawing while preserving original resolution and verifying results with a vision model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liyafeichina](https://clawhub.ai/user/liyafeichina)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide local image edits with Python and PIL, including replacing text, adding watermarks, removing visible content, and checking that edited images keep their original dimensions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe literal substitution into python3 -c snippets could let a malicious image path run local code.

Mitigation: Pass image paths through argv or another structured channel, and validate that paths point to expected local image files before execution.

Risk: Image edits can introduce artifacts, incorrect replacements, or unintended dimension changes.

Mitigation: Compare the edited image with the original using a vision model and confirm that resolution is preserved before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liyafeichina/skills/image-editor)
- [Skill definition](artifact/SKILL.md)
- [Evaluation prompts](artifact/evals/evals.json)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with inline Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes preserving original image resolution and verifying edited output before delivery.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
