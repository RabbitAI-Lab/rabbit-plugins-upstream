## Description:

Use this skill for Workiom requests that read, create, and update data through a connected Workiom account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Workiom schemas, list Workiom apps, lists, records, and metadata, and create records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute remote installer code directly on the user's machine.

Mitigation: Avoid running documented pipe-to-shell installers unless the OOMOL installer source is trusted and separately verified.

Risk: The create_record action changes Workiom data.

Mitigation: Confirm the exact create_record payload and intended effect with the user before running the action.

## Reference(s):

- [Workiom homepage](https://workiom.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-workiom)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance, Configuration]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data from Workiom connector actions.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
