## Description:

Helps agents generate videos from text prompts, reference media, or first and last frames using the dLazy-hosted Wan 2.7 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in requesting video generation from prompts, reference images or videos, and first or last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy-hosted services for generation.

Mitigation: Review prompts and media for sensitive content before submission.

Risk: Using the service requires a dLazy API key.

Mitigation: Protect the key and rotate or revoke it in the dLazy dashboard if needed.

Risk: A global CLI installation persists on the local system.

Mitigation: Use the documented npx option if a persistent global install is not wanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides requests that return hosted generation results or an asynchronous task ID.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
