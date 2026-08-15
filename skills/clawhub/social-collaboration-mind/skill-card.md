## Description:

Social Collaboration Mind helps agents infer collaborator state from expertise, confidence, workload, trust, and mood signals, then choose an adaptive collaboration strategy such as delegate, consult, monitor, pair, or avoid.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill in multi-agent and human-agent collaboration workflows to select an action posture based on collaborator readiness, trust, and communication tone signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner module can persist usage history, error notes, and user preferences in learned_patterns.json.

Mitigation: Avoid recording sensitive task details, review or clear the memory file regularly, and remove or disable scripts/learner.py and learned_patterns.json when persistent personalization is not required.

Risk: Collaboration strategy can be wrong when partner signals are distorted, stale, or self-reported inaccurately.

Mitigation: Cross-check important decisions with independent quality signals or human review before delegating critical work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/social-collaboration-mind)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The included CLI emits a JSON strategy object with strategy, reason, tone, and watch fields.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
