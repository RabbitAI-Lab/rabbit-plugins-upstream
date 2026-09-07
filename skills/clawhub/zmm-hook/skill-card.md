## Description:

Opening-hook specialist for short-video and X-post openings: it first checks whether the source content has enough substance, then diagnoses or generates concise hook candidates with the principle used for each candidate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and content operators use this skill to test whether a draft or topic has enough substance for a strong opening, then generate or refine the first five seconds of a short video or the first line of an X post. It is intended for content-hook critique, candidate generation, and practical revision guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retain user feedback and writing preferences across sessions.

Mitigation: Review or disable the memory write-back behavior before use when drafts, strategy, or personal preferences should not be stored.

Risk: Mutable external vault files can override packaged rules.

Mitigation: Install only with a trusted vault setup, and review any external rule files the skill is expected to read before relying on its guidance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iamzifei/skills/zmm-hook)
- [规则卡](references/规则卡.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown prose with structured diagnostics and hook candidates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask one focused follow-up question when audience or source material is missing; may produce six grouped hook candidates with principle labels.]

## Skill Version(s):

0.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
