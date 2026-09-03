## Description:

Generate high-quality images with Vidu Q2 from text prompts and optional reference images through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to invoke Vidu Q2 image generation from an agent workflow, including text-to-image generation and optional image-to-image references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image references supplied to the skill can be uploaded to dLazy's hosted service.

Mitigation: Use the skill only for intended Vidu/dLazy image generation requests and avoid passing sensitive prompts or local media unless upload is acceptable.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Store credentials only on trusted systems, use the documented environment variable for per-invocation use when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns image result URLs or asynchronous task identifiers, and can optionally save generated assets to a local path.]

## Skill Version(s):

1.3.11 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
