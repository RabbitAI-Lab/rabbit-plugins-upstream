## Description:

A comprehensive generation skill that helps agents generate images, videos, and audio by selecting and invoking the appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route image, video, and audio generation requests through dLazy models. The skill helps an agent choose the relevant dLazy CLI command, provide authentication guidance, and work with generated media result URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate broadly for ordinary generation requests and may use saved credentials for billable dLazy API calls.

Mitigation: Install only when dLazy should handle those requests, confirm before actions that may consume paid credits, and surface insufficient-balance errors to the user.

Risk: Local image, video, or audio paths supplied to generation commands may be uploaded to dLazy media storage.

Mitigation: Confirm user intent before sending local media files, especially files that may contain private, confidential, or regulated content.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Prefer per-invocation use of the DLAZY_API_KEY environment variable when appropriate, and rotate or revoke saved keys if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference hosted image, video, audio, or SVG result URLs returned by dLazy services.]

## Skill Version(s):

1.3.6 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
