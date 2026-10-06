## Description:

A multi-agent writing workflow for academic papers, in-depth articles, and industry analysis, with evidence review, peer review, and advisory publication matching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Researchers, writers, and analysts use this skill to plan, research, draft, audit, and revise long-form papers and articles, then review the final text and supporting evidence before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries or draft material may be sent to external services depending on the user's choices.

Mitigation: Choose the local/no-external option for sensitive work and approve any external research before use.

Risk: The workflow creates a sizeable project file tree, including status and review records that may contain run details.

Mitigation: Confirm the proposed project files before starting, and redact status files before sharing.

Risk: Optional operational telemetry can create additional heartbeat records.

Mitigation: Leave telemetry disabled unless these records are needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quick start](QUICKSTART.md)
- [Pipeline guide](references/pipeline-readme.md)
- [Deliverables and review boundaries](references/deliverables.md)
- [External services and consent](references/_shared/真源/external-services.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown drafts and final articles with evidence and review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped drafts, status files, audit reports, and optional SVG figures.]

## Skill Version(s):

2.15.12 (source: SKILL.md metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
