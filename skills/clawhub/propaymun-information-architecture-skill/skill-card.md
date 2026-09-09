## Description:

Guide information architecture (IA) design and review when users ask for IA or need to organize, label, relate, or find product information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kamroncorp](https://clawhub.ai/user/kamroncorp)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Product, design, content, and engineering teams use this skill to turn product briefs and supplied evidence into clear, evidence-aware information architecture. It helps define information domains, labels, relationships, navigation, search, permissions, governance, validation steps, and optional local IA artifacts when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Information architecture recommendations can be mistaken for validated product evidence.

Mitigation: Treat AI-generated IA as a hypothesis until supported by appropriate product evidence or validation, and keep consequential unknowns visible.

Risk: Optional helpers may create local IA outputs that users did not intend to persist.

Mitigation: Run helpers only on request with explicit input and output paths, preserve existing files, and review generated artifacts before reuse.

Risk: Persistent workspace instructions can continue shaping later agent behavior.

Mitigation: Review the workspace-kit instructions before installing them in a Project, Gem, or custom agent, and remove them when that behavior is no longer wanted.

## Reference(s):

- [Capability-aware execution and output routing](references/capability-routing.md)
- [IA deliverables and semantic model](references/deliverables.md)
- [Optional IA diagramming](references/diagramming.md)
- [Discovery and low-effort interaction](references/discovery.md)
- [Evidence and uncertainty](references/evidence.md)
- [IA foundations and decision rules](references/ia-foundations.md)
- [Contextual localization](references/localization.md)
- [Modeling and option generation](references/modeling.md)
- [IA validation and measurement](references/validation.md)
- [Visual Builder Handoff](references/visual-builder-handoff.md)
- [Semantic IA schema](schema/semantic-ia.schema.json)
- [ProPaymun IA workspace kit v0.4.1](propaymun-ia-workspace-kit-v0.4.1.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, structured IA JSON, HTML, builder handoff Markdown, or shell commands when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local helpers use explicit input and output paths, require no network or credentials, and preserve existing output files.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact metadata version 0.4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
