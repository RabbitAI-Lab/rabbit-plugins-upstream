## Description:

Clone a reference voice and generate new text reading audio with Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to clone a permitted reference voice and generate spoken audio for supplied text through the dLazy Vidu Audio Clone service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media paths may be sent to dLazy-hosted services.

Mitigation: Avoid sensitive inputs unless approved for this service, and review what will be uploaded before running generation.

Risk: Voice cloning can misuse a person's voice without permission.

Mitigation: Use only reference audio that the user has the right and consent to use.

Risk: The skill depends on the external @dlazy/cli npm package and dLazy API endpoints.

Mitigation: Prefer npx or an isolated install, keep the pinned CLI version, and install only when the dLazy publisher and package are trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy Homepage](https://dlazy.com)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated file URLs or an asynchronous task ID through the dLazy CLI.]

## Skill Version(s):

1.3.14 (source: release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
