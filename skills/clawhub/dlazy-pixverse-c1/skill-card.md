## Description:

Helps agents generate PixVerse C1 videos from text prompts, images, reference images, or first and last frames through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short PixVerse C1 videos from text or image inputs and retrieve the generated results through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's hosted service.

Mitigation: Use only when cloud processing is acceptable; avoid providing sensitive prompts or media.

Risk: The external CLI may store an API key locally, and generation may consume credits.

Mitigation: Protect and rotate credentials, use per-invocation credentials if preferred, and check the cost estimate before generating.

Risk: Installing an external CLI introduces third-party software into the environment.

Mitigation: Review the pinned npm package and declared source before installing in sensitive environments.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI source (declared in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples and JSON result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs or local saved files may be returned by the external service; asynchronous requests return a task ID for later retrieval.]

## Skill Version(s):

1.2.24 (source: server-resolved release evidence; bundled skill frontmatter states 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
