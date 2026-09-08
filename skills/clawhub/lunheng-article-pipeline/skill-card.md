## Description:

Lunheng is a Chinese multi-agent workflow for producing evidence-based long-form articles, academic papers, business reviews, and industry analysis through staged research, outline review, drafting, critique, audit, and final inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Writers, analysts, editors, and research-oriented agents use this skill to coordinate Chinese long-form writing projects that need evidence collection, human checkpoints, structured drafts, audit reports, and final delivery artifacts. It is best suited to topics requiring published sources, data, examples, and multi-party viewpoints rather than short answers or purely creative writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow writes multiple project files and may perform external web research.

Mitigation: Run it only in a workspace where file writes are expected, confirm the project directory during Phase 0, and approve external research scope before execution.

Risk: Subagent privilege limits are advisory in the skill documentation, so no-shell behavior is not mechanically guaranteed by the skill alone.

Mitigation: Use a host profile that mechanically denies exec, process, browser automation, apply_patch, cron, memory_store, and cross-session messaging before installing or running the skill.

Risk: External web pages and user-supplied materials can contain misleading instructions or prompt-injection content.

Mitigation: Treat external content only as evidence, ignore instructions found in retrieved materials, and require source verification before using facts in drafts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](artifact/QUICKSTART.md)
- [Pipeline readme](artifact/references/pipeline-readme.md)
- [Permissions and tool boundaries](artifact/references/permissions.md)
- [Deliverables](artifact/references/deliverables.md)
- [M-Gate Algorithm](artifact/references/_shared/M-Gate-Algorithm.md)
- [Failure modes](artifact/references/_shared/failure-modes.md)
- [Format export](artifact/references/_shared/format-export.md)
- [Chinese AI trace checker](artifact/references/checkers/中文AI痕迹-checker.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Markdown project files, research cards, data cards, case cards, outlines, drafts, audit reports, checklists, and final delivery notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes project artifacts under run/<project name>/, uses web research when approved, and supports optional image or memory-assisted steps only after Phase 0 consent.]

## Skill Version(s):

2.10.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
