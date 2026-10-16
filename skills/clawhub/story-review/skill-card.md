## Description:

Reviews Chinese-language fiction from multiple perspectives, identifying story, character, prose, and continuity issues with evidence-backed revision suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Authors and editors use this skill to review Chinese-language fiction for plot, character, style, and continuity problems. It can coordinate multiple reviewers when trusted local reviewer agents are available or work alone otherwise.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Multi-reviewer mode may run project-provided reviewer agents after only basic file validation in an untrusted story project.

Mitigation: Check that local reviewer agent files and their tool permissions come from a trusted setup before using full or lean mode; use solo mode for untrusted projects.

Risk: Review workflows may write project-local state and tracking files.

Mitigation: Review the proposed project changes and keep copies of state or tracking files before running batch or multi-reviewer workflows.

## Reference(s):

- [ClawHub story-review release](https://clawhub.ai/worldwonderer/skills/story-review)
- [Project link listed in skill metadata (not verified provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Review quality rubric](references/quality-rubric.md)
- [Reviewer prompts and synthesis](references/agent-prompts.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review report with prioritized findings and revision suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update project-local review state and tracking files when applicable.]

## Skill Version(s):

1.1.35 (source: ClawHub release metadata; bundled SKILL.md says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
