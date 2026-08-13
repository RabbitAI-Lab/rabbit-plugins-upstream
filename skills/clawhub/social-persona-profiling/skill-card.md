## Description:

Profiles people from provided social-media traces to produce speculative, evidence-weighted persona reads, relationship analysis, and non-directive next-step guidance with explicit confidence grading and privacy safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when they have concrete, consent-aware social profile or chat context and need a structured, hypothesis-level read of personality signals, relationship dynamics, credibility, or scam risk. Outputs are exploratory discussion points and must not be used for diagnosis, manipulation, public shaming, or consequential decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inputs can include personal social traces such as avatars, chat logs, shared content, and profile details.

Mitigation: Use concrete, consent-aware context, keep inputs minimal, avoid private third-party content without consent, and do not restate identifiable details unnecessarily.

Risk: Personality and relationship inferences from limited social traces can be false positives or overconfident hypotheses.

Mitigation: Grade every conclusion by confidence, treat outputs as working hypotheses, cross-check with direct interaction, and avoid using hypotheses as a basis for action.

Risk: Psychological frameworks may be mistaken for diagnosis or reliable mental-health assessment.

Mitigation: Do not diagnose or label mental-health conditions; if distress signs appear, suggest professional help instead of making clinical claims.

Risk: Profiling could be misused for hiring, credit, legal, medical, public shaming, manipulation, or relationship-ending decisions.

Mitigation: Refuse manipulative, discriminatory, or consequential uses and frame any next-step guidance as exploratory options for the user's judgment.

## Reference(s):

- [Psychology Framework Toolbox](artifact/references/psych-frameworks.md)
- [Moderators](artifact/references/moderators.md)
- [Consulting Playbook](artifact/references/consulting-playbook.md)
- [ClawHub skill release](https://clawhub.ai/haiyangchenbj/skills/social-persona-profiling)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with confidence-tiered analysis and scenario-based guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Speculative, non-diagnostic, non-directive, and grounded in user-provided social traces.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
