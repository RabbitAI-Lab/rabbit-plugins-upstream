## Description:

Circle enables an agent to operate Circle communities through the OOMOL oo CLI, including reading community data and running supported Circle connector actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to inspect Circle connector schemas and retrieve or manage Circle community, member, space, and post data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can ask users to execute a remote installer.

Mitigation: Review the installer path before enabling the skill and prefer a verified, versioned, checksum- or signature-checked oo CLI installation method.

Risk: Circle community, member, post, and space reads can expose sensitive community data.

Mitigation: Treat returned Circle data as sensitive and limit use to authorized accounts and requested records.

Risk: Some Circle actions can change state, and action labels may be ambiguous.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect before running any state-changing action.

## Reference(s):

- [Circle homepage](https://circle.so)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector calls can return JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
