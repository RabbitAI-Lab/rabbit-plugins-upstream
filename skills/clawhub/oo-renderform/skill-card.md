## Description:

RenderForm (renderform.io) lets an agent inspect RenderForm connector schemas, list templates and results, check usage, render images or PDFs, and capture website screenshots through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate RenderForm through the oo CLI after connecting a RenderForm account in OOMOL. It supports template and result lookup, usage checks, image or PDF rendering, and screenshot generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute a remote installer directly in the shell.

Mitigation: Install the oo CLI only from a reviewed source, or download and inspect or verify the installer before executing it.

Risk: RenderForm actions can consume credits through the connected OOMOL account.

Mitigation: Confirm payloads for rendering and screenshot actions before execution and monitor account usage or billing limits.

Risk: Connector action schemas may change over time.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing each connector payload.

## Reference(s):

- [RenderForm homepage](https://renderform.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL RenderForm connection](https://console.oomol.com/app-connections?provider=renderform)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include normalized data, execution IDs, request IDs, file URLs, echoed requests, pagination details, usage summaries, and template metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
