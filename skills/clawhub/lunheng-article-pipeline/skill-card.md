## Description:

学术论文/深度长文/行业分析流水线：三角验证+M门+中文AI痕迹闸；exec 禁用为声明式纪律，检索/封面外发与 run/项目名/.tmp/ 周期性写盘须 Phase 0 同意。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, analysts, and writers use this skill to coordinate a human-reviewed multi-agent workflow for academic papers, long-form analysis, and industry reports. The workflow supports evidence collection, outline development, drafting, critique, audit, peer review, and final inspection with explicit consent gates for file writes and external services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default multi-agent workflow relies on soft permission discipline, so host tool access may be broader than the skill's declared role boundaries.

Mitigation: Use a hardened host configuration or single-controller mode for confidential, regulated, client, or unpublished work, and review the permissions guidance before deployment.

Risk: The workflow writes many project files and keeps sensitive runtime status locally during execution.

Mitigation: Run it only in an appropriate workspace, review the Phase 0 file-write plan, and redact or exclude status.md before archiving or sharing project materials.

Risk: Web research and optional cover generation can send search terms, target URLs, or prompts to external services after consent.

Mitigation: Decline unnecessary external services, use the explicit Phase 0 consent gates, and avoid sending sensitive unpublished material to external providers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [SKILL.md](SKILL.md)
- [Quickstart](QUICKSTART.md)
- [Pipeline manual](references/pipeline-readme.md)
- [Permissions and capability boundaries](references/permissions.md)
- [External services and runtime safety](references/_shared/external-services.md)
- [M-Gate algorithm specification](references/_shared/M-Gate-Algorithm.md)
- [Audit checklist](references/_shared/audit-checklist-quickref.md)
- [Deliverables and revision boundaries](references/deliverables.md)
- [Task brief template](references/templates/任务简报-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands]

**Output Format:** [Markdown project files, task briefs, research cards, drafts, audit reports, review reports, final manuscripts, and user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a long-running workspace project tree under run/<project>/ after Phase 0 confirmation; shell commands are presented for human execution rather than agent execution.]

## Skill Version(s):

2.12.40 (source: metadata.openclaw.version and release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
