## Description:

ClawVision East Edition turns a user-selected OpenClaw session into local HTML, Markdown, PowerPoint, and PNG summary exports using local LLM summarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill when they explicitly want to transform selected session history into shareable local visual summaries and export files. The workflow is intended for confirmed visualization/export requests, not generic note-taking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected session history can include secrets, personal data, or internal identifiers that may appear in exported files.

Mitigation: Confirm the requested session and export scope before running the workflow, avoid exporting sensitive sessions without explicit consent, and review generated files before sharing them.

Risk: The skill requires access to session history and local file creation to perform its export workflow.

Mitigation: Install and run it only when those permissions are acceptable for the selected workspace and output directory.

Risk: Local LLM summaries may omit, compress, or misstate details from the original session.

Mitigation: Treat exported summaries as reviewable drafts and compare important claims against the source session before relying on or distributing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/clawvision-ee)
- [Project homepage](https://github.com/monaxamo/clawvision-ee)

## Skill Output:

**Output Type(s):** [Files, Markdown, HTML, PowerPoint, PNG, Guidance]

**Output Format:** [Local HTML, Markdown, PowerPoint, and PNG exports with textual output paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Self-contained HTML with theme and language toggles; PNG screenshots are generated from the local HTML export when requested.]

## Skill Version(s):

1.0.8 (source: server release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
