## Description:

Generates text, answers questions, and supports reasoning with Grok 4.2 through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users invoke the dLazy CLI for text generation, conversational answers, and reasoning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The text-only description conflicts with documented media upload and hosted image-output behavior.

Mitigation: Review the requested inputs and expected outputs before use; provide media files only intentionally.

Risk: Prompts, parameters, and explicitly supplied media can be sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive content unless its transfer to dLazy is approved.

Risk: Using the third-party npm CLI requires storing a dLazy API key locally.

Mitigation: Review the pinned CLI package before installation and protect or revoke the key as needed.

Risk: Broad chat and question-answer triggers may invoke the skill unexpectedly.

Mitigation: Invoke the skill deliberately rather than relying on generic triggers.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Image links]

**Output Format:** [JSON response containing generated outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented example includes a hosted image URL despite the text-only description; asynchronous calls can return a task ID before outputs are available.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
