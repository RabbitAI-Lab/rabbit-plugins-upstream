## Description:

Polish a technical blog draft into an 1000-1200 word, 4-5 section en-US article, preserve technical terms/code, and generate consistent hero + per-section image prompts when the user asks to polish and translate a blog with images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, and content teams use this skill to turn a draft technical post into a polished en-US article and a matching set of hero and section image prompts. It is intended for workflows where the user already has a draft and wants clearer structure, preserved technical meaning, and consistent visual prompt outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Polished drafts and image prompt metadata are saved to disk by default, which can retain unpublished, proprietary, or sensitive draft content.

Mitigation: Use a custom outputDir for sensitive work and delete generated files after review when persistence is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/blog-polish-eng-multi-images)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Structured JSON with paths plus generated Markdown and single-line image prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a polished markdown file path, image file paths or intended filenames, and ordered hero plus section image prompts.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
