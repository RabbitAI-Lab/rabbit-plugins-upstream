## Description:

论衡是一套面向学术论文、商业评论、行业分析和公众号深度长文的多 Agent 写作流水线，通过并行检索、三角验证、M 门、失败模式防御、审计和终检生成可复核的长文交付物。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, researchers, and analysts use this skill to coordinate OpenClaw agents for evidence-backed long-form article production. It is best suited to projects that need published-source research, human checkpoints, structured drafting, independent critique, audit reports, and final Markdown deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default multi-agent mode can continue when spawned workers have dangerous extra tools.

Mitigation: Install only in a workspace and host profile where subagents are acceptable; for sensitive drafts or business data, use single-controller mode or host-level tool allowlists, filesystem containment, and network restrictions.

Risk: The workflow creates and modifies files under run/<project>/ and writes status and heartbeat files during execution.

Mitigation: Review the Phase 0 file-creation disclosure, choose a project name explicitly, and run the skill in a workspace where these project files are expected.

Risk: Research tools and optional services may send search terms, target URLs, prompts, or memory-search data to external providers.

Mitigation: Use the Phase 0 external-service consent options carefully; reject external services or choose local/de-identified alternatives for sensitive or confidential material.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](QUICKSTART.md)
- [Pipeline Runbook](references/pipeline-readme.md)
- [Permissions and Capability Boundaries](references/permissions.md)
- [External Services and Safety Notice](references/_shared/external-services.md)
- [Phase Order](references/_shared/phase-order.yaml)
- [M-Gate Algorithm](references/_shared/M-Gate-Algorithm.md)
- [Asset Index](references/_shared/asset-index.md)
- [Failure Modes](references/_shared/failure-modes.md)
- [G14 Chinese AI Trace Gate](references/gates/14-中文AI痕迹-gate.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Markdown files, status files, audit reports, review reports, evidence cards, optional SVG chart files, and human-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a project tree under run/<project>/ with approximately 15-25 workflow files; external research and optional services are controlled through Phase 0 consent.]

## Skill Version(s):

2.12.32 (source: metadata.openclaw.version, release evidence, QUICKSTART.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
