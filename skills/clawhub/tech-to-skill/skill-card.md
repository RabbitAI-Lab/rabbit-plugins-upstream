## Description:

Distills technical long-form content, papers, and project documentation into agent-callable skills with evidence indexes and temporal tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leogoat2004](https://clawhub.ai/user/leogoat2004)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to convert technical articles, papers, and project documentation into reusable local skill files with What/How/Why sections, evidence references, and timestamps for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reference files may copy excerpts from user-provided source material, including private repositories or internal documents.

Mitigation: Use an output directory you control and review generated skills and references before sharing or installing them elsewhere.

Risk: Generated skills can preserve gaps, inferences, or outdated details from the source material.

Mitigation: Review the candidate list, What/How/Why sections, evidence indexes, and timestamps before relying on or publishing generated skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leogoat2004/skills/tech-to-skill)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [longform-to-skill sub-skill](artifact/sub-skills/longform-to-skill/SKILL.md)
- [paper-to-skill sub-skill](artifact/sub-skills/paper-to-skill/SKILL.md)
- [project-docs-to-skill sub-skill](artifact/sub-skills/project-docs-to-skill/SKILL.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown skill files and reference files, usually SKILL.md, references/*.md, and a batch README.md.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts require user confirmation, source-evidence review, and no automatic installation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
