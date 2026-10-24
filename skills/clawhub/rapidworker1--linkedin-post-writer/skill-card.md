## Description:

Writes LinkedIn posts with a hook, a body and a call to action, measured against the platform's character limits. Use when the user asks for linkedin post writer, linkedin post character limit, linkedin content generator. For US founders, recruiters and B2B marketers who post from their own company pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rapidworker1](https://clawhub.ai/user/rapidworker1)

### License/Terms of Use:

MIT-0

## Use Case:

External US founders, recruiters, and B2B marketers use the skill to draft concise LinkedIn posts with hooks, calls to action, disclosure guidance, and character-limit checks.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The optional Windows app is separate from the bundled workflow, and its safety is not established by this review.

Mitigation: Assess it separately, verify the download before running, and avoid administrator privileges unless necessary.

Risk: The length-check script overwrites length-check.md in the selected output folder.

Mitigation: Use a dedicated output folder or preserve any existing report before running the script.

Risk: The helper counts the entire input file, including template fields, so its count may not match the final post.

Mitigation: Double-check the final post's character count before publishing.

## Reference(s):

- [LinkedIn post rules](references/linkedin-post-rules.md)
- [ClawHub skill release](https://clawhub.ai/rapidworker1/skills/linkedin-post-writer)
- [Publisher homepage (metadata)](https://github.com/rapidworker1)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [LinkedIn post text and a Markdown length-check report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides a full post, three hook options, character-limit results, and disclosure guidance; posting remains manual.]

## Skill Version(s):

1.0.7 (source: frontmatter, server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
