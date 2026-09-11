## Description:

Generates cinematic brand or product ad video clips from a product description or photo using the Ofox video API with a creative brief, prompt, cost estimate, submission, polling, download, and cost report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and developers use this skill to create commercial-style product or brand video ads from a written product description or a product photo. It is intended for non-dialogue ad clips where the user wants guided choices for tone, camera movement, aspect ratio, prompt structure, and cost approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid API key and may send product images, prompts, and ad concepts to Ofox/Seedance.

Mitigation: Use it only when that processing is acceptable, keep OFOX_API_KEY protected, review the cost table, and require explicit approval before generation.

Risk: Security evidence flags a missing external core dependency and an unpinned whole-repo install path.

Mitigation: Review or pin the ofox-video-core dependency and install source before running generation commands.

Risk: Generated ad prompts or clips can be visually inaccurate, monotonous, or unsuitable for publication.

Mitigation: Review the prompt, sampled frames, costs, and final video before publication or customer use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-ad-creative)
- [Clawdis homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-ad-creative)
- [Ofox API key portal](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with prompt text, brief recap, cost table, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, jq, and user approval before paid generation.]

## Skill Version(s):

1.11.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
