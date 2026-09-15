## Description:

Lunheng guides an agent through a human-reviewed workflow for producing evidence-based academic papers, business commentary, industry analysis, and other long-form articles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Writers, researchers, analysts, and operators use this skill to plan, research, draft, review, revise, and package long-form evidence-based articles with human checkpoints. It is best suited to work that needs published sources, data or case evidence, quality review, and clear delivery boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks this release as suspicious because multi-agent spawning rules should be reviewed before installation.

Mitigation: Use single-controller mode unless Phase 0 records explicit multi-agent consent and the OpenClaw host has been hardened for the intended worker permissions.

Risk: The workflow may run for a long time and write many project files, status records, and reports.

Mitigation: Confirm the Phase 0 file list before starting, keep writes inside the declared project workspace, and review generated artifacts before sharing.

Risk: Research and generation steps may send search terms, URLs, prompts, or article content to external services when enabled.

Mitigation: Record external-service choices in Phase 0 and choose the no-web or local-only path for sensitive work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](QUICKSTART.md)
- [Pipeline runbook](references/pipeline-readme.md)
- [Permissions and tool boundaries](references/permissions.md)
- [External services and consent](references/_shared/external-services.md)
- [Phase order](references/_shared/phase-order.yaml)
- [M-Gate algorithm](references/_shared/M-Gate-Algorithm.md)
- [Audit checklist](references/_shared/audit-checklist-quickref.md)
- [G14 Chinese AI trace gate](references/gates/14-中文AI痕迹-gate.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown articles, evidence cards, audit reports, status files, and optional SVG chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates project files under a user-confirmed workspace path after Phase 0 consent; external-service use and multi-agent mode are governed by explicit user choices.]

## Skill Version(s):

2.12.45 (source: metadata.openclaw.version and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
