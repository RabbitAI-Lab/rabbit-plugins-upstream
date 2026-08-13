## Description:

Polish a technical blog draft into an 800-1000 word, 3-4 section zh-CN article, preserve technical terms/code, and generate consistent hero + per-section image prompts when the user asks to polish and translate a blog with images.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Blog authors, developer advocates, and technical content teams use this skill to turn a technical draft into a Simplified Chinese article package with consistent image prompts. Security evidence indicates the current implementation should be treated as draft/demo quality and reviewed before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may leave the source text essentially unchanged while reporting a polished zh-CN package.

Mitigation: Treat outputs as draft/demo material and review the article manually before publication or external sharing.

Risk: Drafts and generated files may be saved persistently under ~/.openclaw/workspace/contentPolished/.

Mitigation: Avoid sensitive drafts unless the output directory is approved, and clean generated files after review.

Risk: Image prompts may be hard-coded rather than derived from the article sections.

Mitigation: Check each prompt against the final article and revise prompts before image generation.

## Reference(s):


## Skill Output:

**Output Type(s):** [markdown, text, files]

**Output Format:** [Markdown file plus structured JSON fields for polishedPath, imagePaths, and imagePrompts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include intended image filenames and text prompts when image generation is not available.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
