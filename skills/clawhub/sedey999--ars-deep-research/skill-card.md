## Description:

Universal deep research agent team for rigorous academic research, literature review, fact-checking, Socratic guided research, systematic review, and optional meta-analysis.

This skill is for research and development only.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

CC BY-NC 4.0

## Use Case:

External researchers, students, and research teams use this skill to scope research questions, search and verify literature, synthesize evidence, assess bias and ethics, and compile academic reports or review artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has a suspicious security verdict because it includes hidden opt-in user-behavior probes and broad local or external processing.

Mitigation: Install only after review, keep optional probes disabled by default, and disclose any response logging or summary carry-forward before enabling them.

Risk: The workflow may read project files, process local PDFs, call bibliographic APIs, and write phase artifacts.

Mitigation: Use explicit user activation and scope confirmation before local file processing, PDF handling, monitoring setup, external provider checks, or shell-dispatched sidecar building.

Risk: Optional cross-model checks can send research material to an external provider.

Mitigation: Require explicit consent that identifies the provider, model, and content class before external verification is used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sedey999/skills/ars-deep-research)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [Attribution](artifact/ATTRIBUTION.md)
- [Mode selection guide](artifact/references/guides/mode_selection_guide.md)
- [Systematic review protocol](artifact/references/guides/systematic_review_protocol.md)
- [Source quality hierarchy](artifact/references/guides/source_quality_hierarchy.md)
- [Cross-model verification](artifact/references/shared/cross_model_verification.md)
- [Literature monitoring strategies](artifact/references/guides/literature_monitoring_strategies.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports, structured research artifacts, review notes, citation markers, and optional configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs vary by mode, including research briefs, APA 7.0 reports, annotated bibliographies, verification reports, PRISMA reports, monitoring digests, and sidecar-style artifacts.]

## Skill Version(s):

2.12.2 (source: evidence.release.version, SKILL.md metadata, and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
