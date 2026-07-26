## Description: <br>
Own Style Writer helps an agent learn a user-provided writing style corpus, keep style sources separate from factual content sources, convert documents with opt-in MinerU or local MarkItDown, and draft only after producing a style profile, content brief, and outline for confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[snowles](https://clawhub.ai/user/snowles) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, writers, editors, and developers use this skill to prepare style and content corpora, generate a style profile and content brief, review an outline, and then draft articles in the user's own style. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read the style and content directories named by the user and write generated corpora and drafts to an output folder. <br>
Mitigation: Use only intended input directories, choose an appropriate output folder, and review generated corpora and drafts before sharing or publishing. <br>
Risk: Using MinerU upload can send local documents to a third-party parsing service. <br>
Mitigation: Allow MinerU upload only for documents that are acceptable to send externally; use local MarkItDown mode for confidential files. <br>
Risk: The local MarkItDown fallback may install or use Python dependencies for document conversion. <br>
Mitigation: In stricter environments, review or pin the Python dependencies before first use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/snowles/skills/own-style-writer) <br>
- [Own Style Writer homepage](https://github.com/snowles/own-style-writer) <br>
- [MinerU API documentation](https://mineru.net/apiManage/docs) <br>
- [MarkItDown project](https://github.com/microsoft/markitdown) <br>
- [Writing principles](references/writing_principles.md) <br>
- [Style profile template](references/style_profile_template.md) <br>
- [Content brief template](references/content_brief_template.md) <br>
- [Outline review template](references/outline_review_template.md) <br>
- [Quality check template](references/quality_check_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown files, inline shell commands, and structured writing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create converted corpora, manifest.json, conversion_errors.json, style profiles, content briefs, outlines, drafts, quality reports, and writing review memory in user-selected output directories.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
