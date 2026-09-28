## Description:

Guides an agent to use dLazy's hosted VideoRetalk service to match a talking person's mouth movements to a supplied voice track, optionally selecting a face with a reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to retime a speaker's lip movements in an existing video to new speech, with an optional face reference when multiple people appear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input video, audio, and optional face images may be uploaded to dLazy's hosted service.

Mitigation: Use only media you are comfortable sharing with dLazy and review the service terms before submitting sensitive material.

Risk: Authentication can store an API key locally, and the skill relies on an external CLI package.

Mitigation: Protect the local key, review the CLI package and source before use, and prefer the documented pinned npx command if a persistent global install is undesirable.

Risk: Documentation examples contain minor inconsistencies that may mislead users about the input flags or returned media type.

Mitigation: Check the installed CLI's help and inspect actual task responses rather than relying on the examples alone.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON task responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service provides a generated-media URL; the CLI can optionally save the result locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.22 (source: ClawHub release; source skill frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
