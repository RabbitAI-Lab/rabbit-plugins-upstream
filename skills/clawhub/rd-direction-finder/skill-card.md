## Description:

Given an engineering or technical problem statement, this skill analyzes requirements across demand drivers, bottlenecks, and solution paths, identifies distinct technical challenges and R&D directions, searches patent, paper, and web sources, and produces structured Markdown, JSON, and HTML research-direction reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and R&D planning teams use this skill to turn a 100-400 character engineering problem description into candidate research directions backed by patent, paper, and web evidence. It is suited for early project scoping and technology route exploration, not single-document review, FTO analysis, or open-ended intelligence gathering without a problem statement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Problem descriptions may be sent to PatSnap, patent, paper, and web search services during report generation.

Mitigation: Redact trade secrets, customer-sensitive details, and other confidential information before using the skill.

Risk: Generated Markdown, JSON, and HTML reports may persist locally and contain the submitted problem statement and search-derived evidence.

Mitigation: Delete, relocate, or otherwise manage generated reports according to the user's retention and confidentiality requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/rd-direction-finder)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [Output paths](assets/paths.md)
- [Payload schema](assets/payload-schema.md)
- [Report template](assets/report-template.md)
- [Workflow reference](assets/workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, Shell commands, Guidance]

**Output Format:** [Markdown report plus structured payload JSON and rendered HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses problem_text and optional max_directions; default output paths are under @session/reports with date-stamped filenames.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
