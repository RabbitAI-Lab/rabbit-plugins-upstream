## Description:

Verify Before Answer prompts an agent to check factual, comparison, capability, and time-sensitive claims against search results, documentation, or runtime evidence before responding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[padepa](https://clawhub.ai/user/padepa)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users can use this skill to reduce unsupported factual answers by making verification the default for factual, comparison, capability, relationship, and recent-status questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification may involve local project or runtime checks whose outputs could contain sensitive workspace details.

Mitigation: Review command outputs and source excerpts before sharing them, and omit sensitive details that are not needed to support the answer.

Risk: Search results or documentation may be stale, incomplete, or contradictory.

Mitigation: Prefer official sources, state the evidence date or boundary for time-sensitive claims, and distinguish lack of evidence from verified negative findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/padepa/skills/verify-before-answer)
- [Publisher profile](https://clawhub.ai/user/padepa)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with optional inline commands and source notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Encourages explicit source boundaries and distinguishes unsupported claims from verified negative findings.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
