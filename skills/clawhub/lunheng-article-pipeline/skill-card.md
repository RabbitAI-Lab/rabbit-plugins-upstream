## Description:

lunheng-article-pipeline coordinates OpenClaw subagents to produce Chinese academic papers and long-form analysis with literature, data, case evidence, review gates, and human approval checkpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Writers, researchers, and developers use this skill to run a structured Chinese long-form writing workflow for academic papers, business commentary, industry analysis, and public-account essays. It is best suited to evidence-heavy work that benefits from literature, data, case retrieval, critique, audit, revision, and final review stages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A documented fallback conflicts with the skill's permanent exec/process denial by telling the coordinator to use host command execution.

Mitigation: Deploy only where exec/process denial is enforced by the OpenClaw host for the coordinator and all subagents, and review the skill before installation.

Risk: Research prompts, draft content, keywords, or URLs may be sent to external search or extraction services during evidence gathering.

Mitigation: For sensitive or proprietary work, choose the local/no-external option in Phase 0 and avoid optional image generation or additional data-source integrations unless the data flow is acceptable.

Risk: The workflow writes multiple project artifacts and status files while coordinating subagents.

Mitigation: Run the skill in a dedicated project workspace, enforce the documented run/<project>/ path boundary, and review generated outputs before relying on them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](QUICKSTART.md)
- [Pipeline readme](references/pipeline-readme.md)
- [Glossary](references/glossary.md)
- [Deliverables](references/deliverables.md)
- [Operations](references/operations.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown files and structured status, evidence, audit, revision, and final-delivery reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces long-form Chinese writing artifacts, evidence cards, review reports, and human approval checkpoints; optional image and memory features require explicit Phase 0 consent.]

## Skill Version(s):

2.6.5 (source: frontmatter and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
