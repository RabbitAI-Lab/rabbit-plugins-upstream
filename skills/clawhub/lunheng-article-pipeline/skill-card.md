## Description:

学术论文、深度长文和行业分析流水线，使用三角验证、M 门审计和中文 AI 痕迹闸，并要求检索在 Phase 0 明示同意后执行。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users, writers, analysts, and researchers use this skill to coordinate long-form Chinese-first article, paper, and industry-analysis workflows that need evidence collection, outline review, drafting, critique, audit, and final inspection. It is best suited to fact-heavy work where the user can approve scope, external-service use, and key review gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow creates and updates many project files under run/<project>/ during normal operation.

Mitigation: Use Phase 0 to review the planned project path and generated files before the workflow enters Phase 1.

Risk: Research keywords, target URLs, or draft content may be sent to configured external providers when external lookup or optional image generation is approved.

Mitigation: For confidential work, choose the local or no-external Phase 0 option and decline optional image generation.

Risk: The documented denied-tool list is declarative and depends on host-side policy for mechanical enforcement.

Mitigation: Run the skill in a host configuration that enforces the desired tool policy, especially for sensitive projects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](QUICKSTART.md)
- [Pipeline overview](references/_shared/pipeline-overview.md)
- [Phase order](references/_shared/phase-order.yaml)
- [Permissions](references/permissions.md)
- [External services](references/_shared/external-services.md)
- [M-Gate Algorithm](references/_shared/M-Gate-Algorithm.md)
- [G14 Chinese AI-trace gate](references/gates/14-中文AI痕迹-gate.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown documents, structured status records, review reports, and handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates a project tree under run/<project>/ after Phase 0 confirmation; may coordinate subagents and optional external lookups according to user choices.]

## Skill Version(s):

2.12.35 (source: server release metadata and metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
