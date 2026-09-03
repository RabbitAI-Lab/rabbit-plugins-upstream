## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative, with support for image, video, audio, and first/last-frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short video assets through dLazy's hosted Seedance 2.5 service from prompts and optional image, video, audio, or first/last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may leave the local machine for processing by dLazy's hosted service.

Mitigation: Use only data appropriate for a third-party cloud service and review dLazy service terms before sending sensitive prompts or media.

Risk: Login can store a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials in stricter environments, and rotate or revoke organization keys when needed.

Risk: The skill depends on a pinned third-party npm package and hosted API endpoints.

Mitigation: Review the pinned npm package and source repository before installation in environments with supply-chain requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [JSON result metadata with generated media URLs, plus optional saved media files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode may return a generateId for polling; prompts and referenced media are processed by dLazy's hosted service.]

## Skill Version(s):

1.2.7 (source: server release evidence; artifact frontmatter and install spec reference 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
