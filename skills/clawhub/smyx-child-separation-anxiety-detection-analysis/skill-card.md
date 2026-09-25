## Description:

Analyzes home entrance or kindergarten gate video to identify crying, clinging, and resistance behaviors and summarize a child's separation-anxiety level as mild, moderate, or severe.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, teachers, and developers can use this skill to process drop-off videos from a home entrance or kindergarten gate and receive behavior observations, anxiety-level summaries, and supportive next-step guidance. The skill is intended for visual behavior analysis and friendly reminders, not psychological diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive videos of children and links analysis to a cloud service.

Mitigation: Use only with explicit parent or guardian consent for cloud processing and report retention, and limit inputs to appropriate drop-off scenes.

Risk: Identity tokens and local records may persist after use.

Mitigation: Run in a contained workspace and delete or revoke local database and token files when analysis is complete.

Risk: The security guidance warns against shared writable locations until the import-path issue is fixed.

Mitigation: Deploy from a dedicated, non-shared workspace and review import paths before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-separation-anxiety-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report or JSON-style structured analysis from API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior metrics, anxiety-level labels, report links, and recommended parent or teacher actions.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
