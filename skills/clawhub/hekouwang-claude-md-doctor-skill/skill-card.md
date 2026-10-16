## Description:

Audits AGENTS.md and CLAUDE.md as agent runtime configuration, producing a scorecard and prioritized fixes with optional user-approved edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to review project agent instructions for clarity, concision, broken document pointers, and exposed secrets, then prioritize improvements. Changes to project files require user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated checks can misclassify project-specific instructions or document pointers.

Mitigation: Review the reported findings and proposed edits before approving changes.

Risk: The optional doctor-suite helper also checks project skills and the local environment.

Mitigation: Use the standard check.py workflow for routine reviews; run the suite only if the broader checks are wanted.

Risk: Unpinned Docker images may change between runs.

Mitigation: Pin the image version or digest when reproducible checks matter.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-md-doctor-skill)
- [Project homepage](https://github.com/huiyonghkw/hekouwang-claude-md-doctor-skill)
- [Doctor suite guide](references/doctor-suite.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Code]

**Output Format:** [Markdown scorecard and prioritized recommendations; optional JSON check report and user-approved configuration edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The checker is read-only; proposed file changes require user consent.]

## Skill Version(s):

1.3.3 (source: release metadata, frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
