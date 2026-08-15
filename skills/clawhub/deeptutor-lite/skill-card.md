## Description:

DeepTutor 轻量辅导台 helps agents run a lightweight personalized tutoring workflow with learner memory, mastery tracking, calibrated practice, multi-perspective discussion, cited explanations, review triggers, and Anki handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shenxianxuexifa](https://clawhub.ai/user/shenxianxuexifa)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, tutors, and agent users use this skill for long-running one-to-one or small-group tutoring where the agent should remember learner weaknesses, track mastery, choose practice difficulty, ground explanations in cited sources, and trigger review or Anki follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to keep local student learning profiles over time.

Mitigation: Use non-sensitive student identifiers, avoid storing unnecessary personal details, review workspace access, and periodically review or delete tutor_memory files when retention is no longer needed.

Risk: Generated tutoring guidance may be incorrect, overconfident, or based on incomplete learner history.

Mitigation: Review cited sources, avoid fabricated memory or mastery values, and have a qualified educator validate high-stakes academic guidance.

## Reference(s):

- [Skill README](artifact/README.md)
- [Skill Instructions](artifact/SKILL.md)
- [DeepTutor](https://deeptutor.info)
- [OpenMAIC DOI](https://doi.org/10.1007/s11390-025-6000-0)
- [ClawHub Skill Page](https://clawhub.ai/shenxianxuexifa/skills/deeptutor-lite)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown tutoring guidance with optional local memory notes, review plans, Anki handoff instructions, and HTML visualization suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose updates to tutor_memory files; does not require an external LLM key by default.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
