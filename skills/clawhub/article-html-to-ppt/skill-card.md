## Description: <br>
Use when turning articles, docs, PRDs, or specs into polished editable PPT decks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[skillmelody](https://clawhub.ai/user/skillmelody) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content teams, and business users use this skill to convert articles, Markdown, HTML, PRDs, specs, and review-approved manuscripts into editable slide decks with content locks, style contracts, builder selection, and verification reports. It can produce local PPTX decks by default and can route to Feishu/Lark Slides when the user explicitly asks for cloud delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local deck-building helper scripts can delete chosen output directories. <br>
Mitigation: Run the skill inside a fresh project directory, keep work and output paths scoped to that directory, and do not point outputs at existing important folders. <br>
Risk: The macOS PowerPoint renderer handles paths unsafely for unusual filenames. <br>
Mitigation: Avoid macOS PowerPoint rendering with unusual filenames; use normalized filenames or another verified renderer until path escaping is fixed. <br>
Risk: Feishu/Lark export can send source content, generated slide text, and metadata to a cloud workspace. <br>
Mitigation: Use Feishu/Lark export only after confirming the destination, sharing boundary, and suitability of the content for that cloud service. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/skillmelody/skills/article-html-to-ppt) <br>
- [README.en.md](README.en.md) <br>
- [v2.0 Acceptance Report](docs/v2.0-acceptance-report.md) <br>
- [Export Pipelines Reference](references/export-pipelines.md) <br>
- [Production Readiness Gates](references/production-readiness-gates.md) <br>
- [Verification Harness Contract](references/verification-harness.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON contracts and reports, and generated PPTX or companion deck files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write .ppt-work artifacts, PPTX decks, verification reports, render reports, delivery manifests, and optional Feishu/Lark cloud outputs when requested.] <br>

## Skill Version(s): <br>
2.1.4 (source: server release; distribution-only rollback of artifact implementation metadata 2.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
