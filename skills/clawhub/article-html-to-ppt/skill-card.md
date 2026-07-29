## Description: <br>
Build and QA editable PPT decks locally; probes required tools/fonts, runs subprocess renderers in isolated work/output folders, and uses cloud export only with explicit consent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[skillmelody](https://clawhub.ai/user/skillmelody) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, product teams, and knowledge creators use this skill to turn articles, Markdown, HTML pages, PRDs, automation plans, and review-approved manuscripts into editable PPTX, dynamic PPTX, HTML preview, or Feishu/Lark slide deliveries with explicit verification status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A packaging path may recursively delete a caller-supplied output directory. <br>
Mitigation: Use a fresh dedicated output directory for each run and avoid pointing output paths at a workspace root, home directory, project directory, or other existing content. <br>
Risk: The skill reads source documents, writes PPT work/output folders, and launches local renderers. <br>
Mitigation: Run it only in an environment where local deck-building subprocesses are acceptable, keep work directories isolated, and review generated decks and reports before sharing. <br>
Risk: Feishu/Lark export uploads deck content and metadata to a cloud service. <br>
Mitigation: Keep local PPTX export as the default for sensitive material and use Feishu/Lark only after explicit user intent and a pre-upload privacy summary. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/skillmelody/skills/article-html-to-ppt) <br>
- [README.en.md](artifact/README.en.md) <br>
- [v2.1 Release Notes](artifact/docs/v2.1-release-notes.md) <br>
- [v2.1 Release Readiness](artifact/docs/v2.1-release-readiness.md) <br>
- [Production Readiness Gates](artifact/references/production-readiness-gates.md) <br>
- [Export Pipelines](artifact/references/export-pipelines.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON contracts, shell commands, and generated presentation files or delivery manifests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Typical generated artifacts include PPTX decks, dynamic PPTX decks, HTML previews, QA reports, build manifests, delivery manifests, and optional Feishu/Lark links when the user explicitly requests cloud export.] <br>

## Skill Version(s): <br>
2.1.2 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
