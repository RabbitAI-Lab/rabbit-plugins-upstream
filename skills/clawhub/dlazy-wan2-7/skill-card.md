## Description:

Generates videos with Tongyi Wanxiang 2.7 from text prompts, reference images or videos, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can use the dLazy CLI to request short video generation from prompts and optional visual references, including first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and reported that the observed behavior appeared limited to `dlazy login`; it did not establish a connection between that behavior and video generation.

Mitigation: Before relying on generation, review the pinned CLI release and confirm that the command produces the expected video output.

Risk: Prompts and local media supplied to the skill are sent to dLazy-hosted services, and generated media is hosted there.

Mitigation: Avoid sending sensitive prompts or media unless the relevant dLazy service terms and organizational policies allow it.

## Reference(s):

- [dLazy CLI repository (linked in the skill; server-resolved provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Files, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON result envelope with generated media URLs or task status; optionally downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports asynchronous task status and optional local saving of results.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
