## Description:

Helps agents generate videos with Kling V3 Omni from text prompts and optional image or video references through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts and optional visual references, and retrieve generated media through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied for generation are sent to a third-party hosted service.

Mitigation: Only submit prompts and media you are comfortable sharing with dLazy.

Risk: Using the third-party CLI requires an API key stored locally or supplied for a request.

Mitigation: Protect the key and rotate or revoke it when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI repository (listed in skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation results may include hosted media URLs; asynchronous requests return a task identifier.]

## Skill Version(s):

1.3.27 (source: ClawHub release; supplied skill files state 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
