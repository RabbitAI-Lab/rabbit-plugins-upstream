## Description:

Helps agents generate videos from text prompts and optional image, video, audio, or first-and-last-frame references through dLazy's Seedance 2.0 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request cloud-generated videos from text or selected image, video, audio, and frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an external npm CLI requires trusting the package and managing a dLazy API key.

Mitigation: Review the pinned CLI package before installing; protect the API key and revoke it if exposed.

Risk: Prompts and user-selected image, video, or audio files are sent to dLazy's cloud service.

Mitigation: Submit only content approved for external processing, and review dLazy's service terms before uploading sensitive media.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns generated asset URLs or an asynchronous task ID; results can be saved locally.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release; skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
