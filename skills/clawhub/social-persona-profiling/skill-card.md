## Description:

Profiles people from social-media traces across platforms and cultures to produce evidence-weighted persona reads, relationship analysis, credibility assessment, and next-step guidance with explicit confidence grading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze provided social-media profiles, avatars, bios, chat excerpts, and related context for persona profiling, relationship guidance, trust assessment, or scam-detection support. The skill is not suitable for consequential screening, discriminatory decisions, harassment, manipulation, or profiling non-consenting private people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be used for broad third-party personality and trust profiling from limited social traces where consent and context may be incomplete.

Mitigation: Use only material the user has a legitimate right to analyze, avoid profiling non-consenting private people, and state that personality or trust conclusions are weak hypotheses rather than facts.

Risk: Outputs may be misused for consequential or harmful decisions such as hiring, credit, screening, harassment, manipulation, or public judgment.

Mitigation: Refuse manipulative, deceptive, discriminatory, or harmful use cases and do not use the analysis for consequential decisions.

Risk: Social traces can support overconfident or culturally biased readings when age, culture, platform, personality baseline, and generation are not calibrated.

Mitigation: Apply moderator adjustment before interpretation, downgrade unsupported conclusions, use three-tier confidence grading, and filter Barnum-style statements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/social-persona-profiling)
- [Psychology Framework Toolbox](artifact/references/psych-frameworks.md)
- [Moderators](artifact/references/moderators.md)
- [Consulting Playbook](artifact/references/consulting-playbook.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with confidence-graded analysis and action guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should separate objective facts, behavioral inferences, and working hypotheses; action guidance should rely on dependable facts and clearly flagged uncertainty.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.1 and README files say v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
