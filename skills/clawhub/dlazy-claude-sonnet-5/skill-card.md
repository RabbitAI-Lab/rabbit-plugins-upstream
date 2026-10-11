## Description:

Enables agents to generate text and code through dLazy's hosted Claude Sonnet 5 service using prompts and optional image or video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to draft text, generate code, and work through reasoning tasks with optional visual context via dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly supplied files are sent to dLazy's hosted service.

Mitigation: Send only content you are comfortable sharing with dLazy; review files before attaching them.

Risk: The dLazy API key is stored in local CLI configuration and grants access to the user's account.

Mitigation: Protect the local key and revoke or rotate it from the dLazy dashboard if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [JSON response containing generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous task response; content can be saved locally.]

## Skill Version(s):

1.2.29 (source: ClawHub release; artifact frontmatter states 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
