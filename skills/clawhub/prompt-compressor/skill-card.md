## Description:

Helps agents shorten prompts and long context by retaining high-information sentences, constraints, numbers, and code blocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and theory)

## Use Case:

Developers and other agent users can condense long prompts or documents to reduce context use while keeping prominent requirements and technical details available for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compression may omit context needed for important decisions.

Mitigation: Review compressed output against the original before relying on it for consequential work.

Risk: Installation examples fetch code from a public GitHub repository.

Mitigation: Review the retrieved files before installing or running them, and process only text and files you intend to share with the skill.

## Reference(s):

- [Prompt Compressor on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-compressor)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Condensed text with a brief retention check when using the included script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A target retention ratio can be supplied; protected content may cause the result to exceed that ratio.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
