## Description:

Social Persona Profiling helps agents produce evidence-weighted social-persona and relationship analysis from user-provided social-media traces, with confidence grading, moderator calibration, and privacy safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to structure speculative persona, relationship, trust, or scam-risk analysis from limited online traces while preserving confidence labels and privacy boundaries. It is not intended for consequential decisions such as hiring, credit, legal, medical, public shaming, profiling minors, manipulation, or major relationship decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Speculative social-persona analysis may be mistaken for factual psychological assessment or diagnosis.

Mitigation: Keep conclusions evidence-weighted and confidence-labeled, and state that outputs are working hypotheses rather than diagnoses or facts.

Risk: Inputs may include identifiable or sensitive avatars, chat logs, profile details, or social-media traces.

Mitigation: Use only material the user has a legitimate reason to provide, avoid unnecessary sensitive details in outputs, and seek consent where feasible.

Risk: Single-sided relationship or attribution analysis may unfairly characterize a subject who cannot respond.

Mitigation: Disclose the one-sided evidence basis, consider client bias, and require direct verification before acting on any conclusion.

Risk: Outputs could be misused for consequential, manipulative, discriminatory, or harmful decisions.

Mitigation: Decline use cases involving hiring, credit, legal, medical, minors, public shaming, manipulation, or major relationship decisions.

## Reference(s):

- [Consulting Guidance Playbook](artifact/references/consulting-playbook.md)
- [Signal Interpretation Moderators](artifact/references/moderators.md)
- [Psychology Frameworks Toolbox](artifact/references/psych-frameworks.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with confidence labels, structured analysis sections, and exploratory guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-only LLM output; no tool calls, API calls, shell commands, or deterministic scripts are required by the artifact.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
