## Description:

Helps creators diagnose whether a short-video idea has enough substance, then draft opening hooks using expectation and information-gap patterns with the underlying principle labeled.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators use this skill to test whether a short-video or X-post opening has enough substance, then generate or refine concise hook candidates for the first seconds of the content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads shared external vault memory and other referenced local writing-system files.

Mitigation: Review and restrict the mounted vault paths before use, and install it only in workspaces where those files are intended to be available.

Risk: The skill may save user feedback into persistent framework memory.

Mitigation: Avoid providing sensitive feedback unless persistence is acceptable, disabled, or otherwise controlled in the agent environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-hook)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown prose with diagnostics, grouped hook candidates, and short rationale notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for one missing audience or material detail before generating candidates; may record feedback in persistent skill memory when enabled.]

## Skill Version(s):

0.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
