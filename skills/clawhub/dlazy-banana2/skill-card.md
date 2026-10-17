## Description:

Guides agents to generate and edit images from text or reference images using dLazy's Nano Banana 2.0 CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users generate new images from prompts or edit images using references through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local reference images sent to the hosted service may contain sensitive information.

Mitigation: Use only intended content and avoid uploading sensitive prompts or media.

Risk: Login stores an API key locally, and generated outputs are hosted by dLazy.

Mitigation: Protect and rotate the API key as needed; treat hosted output links as potentially shareable.

Risk: A global CLI installation persists on the machine.

Mitigation: Use the documented pinned npx invocation if a global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Text guidance and CLI JSON responses containing hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be saved locally; asynchronous runs return a task ID.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; embedded skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
