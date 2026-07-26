## Description: <br>
Compare two sources to find shared and divergent principles -- discover what survives independent observation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leegitw](https://clawhub.ai/user/leegitw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to compare two text sources or extraction outputs, identify shared principles, separate source-specific ideas, and flag divergent claims for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shared or aligned principles can still be incorrect because the skill compares structure, not truth. <br>
Mitigation: Use the comparison as analytical support and verify important claims against the original sources before acting on them. <br>
Risk: Input content is processed by the user's configured agent model. <br>
Mitigation: Provide only content suitable for that agent model and deployment trust boundary. <br>
Risk: The release evidence notes a documentation inconsistency about whether review notes might be written to `requires_review.md`. <br>
Mitigation: Treat any `requires_review.md` mention as ambiguous unless the publisher clarifies whether it is a label or an actual file write. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leegitw/skills/principle-comparator) <br>
- [Skill homepage](https://github.com/live-neon/skills/tree/main/pbd/principle-comparator) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [Markdown prose with structured JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include comparison categories, confidence labels, N-count validation, divergence notes, and next-step guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
