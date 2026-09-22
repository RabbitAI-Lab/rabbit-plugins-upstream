## Description:

论衡 is a multi-agent pipeline for producing academic papers, deep long-form writing, and industry analysis with evidence gathering, human checkpoints, peer review, audit gates, and publication-channel suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

External users, writers, analysts, and research teams use this skill to coordinate a structured long-form writing workflow that collects evidence, drafts and revises an article, runs critique and audit stages, and prepares publication-oriented deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can send search terms, URLs, and selected retrieval requests to external research services when approved.

Mitigation: Use the no-external-services or local option for confidential work, decline optional external services in Phase 0, and remove secrets or identifying details from prompts and source material.

Risk: The skill creates and modifies a multi-file project tree under run/<project>, including drafts, status records, audits, and final deliverables.

Mitigation: Review the Phase 0 file creation list and project name before starting; keep writes confined to the workspace project tree.

Risk: Tool boundaries are declared by the skill, while hard enforcement depends on the host's tool policy and sandbox configuration.

Mitigation: Use host-level allow/deny and sandbox policy for hard enforcement, and review the skill's capability self-check and status reports during execution.

Risk: Long-running multi-agent writing can produce incorrect citations, stale data, or overconfident conclusions if evidence is weak.

Mitigation: Use the built-in evidence cards, audit gates, peer review, and final human review before publishing or relying on the output.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](QUICKSTART.md)
- [Pipeline overview](references/_shared/真源/pipeline-overview.md)
- [Permissions and capability boundaries](references/permissions.md)
- [External services and pre-run safety notice](references/_shared/真源/external-services.md)
- [Deliverables, gates, and failure modes](references/deliverables.md)
- [Asset index](references/_shared/真源/asset-index.md)
- [M-Gate algorithm](references/_shared/真源/M-Gate-Algorithm.md)
- [G14 Chinese AI-trace gate](references/gates/14-中文AI痕迹-gate.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown project files, evidence cards, drafts, audit and review reports, status records, and optional SVG chart files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow writes a project tree under run/<project> after Phase 0 confirmation and may use consent-gated external research services.]

## Skill Version(s):

2.12.70 (source: evidence.release.version and metadata.openclaw.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
