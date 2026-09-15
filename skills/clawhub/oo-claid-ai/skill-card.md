## Description:

Claid AI helps agents inspect live action schemas and run Claid image-editing actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to inspect Claid AI action schemas and run image-editing actions through an OOMOL-connected account without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute local code if run automatically or from an untrusted source.

Mitigation: Do not let an agent automatically run the installer commands; install the OOMOL CLI only from a trusted, verifiable source.

Risk: Image-editing actions are write actions and may change Claid AI state or consume account resources.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

Risk: Action schemas are live, so stale assumptions about payload fields can cause failed or unintended requests.

Mitigation: Fetch the authoritative connector schema before constructing each action payload.

## Reference(s):

- [Claid AI homepage](https://claid.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live connector schemas should be inspected before constructing payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
