## Description:

fal.ai (fal.ai). Use this skill for ANY fal.ai request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate fal.ai through an OOMOL-connected account: inspect live action schemas, discover models and pricing, submit queued model requests, monitor status, cancel requests, and retrieve results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote shell installer commands for the oo CLI.

Mitigation: Do not let an agent automatically run curl|bash or irm|iex; install the oo CLI only from a trusted, verifiable source, preferably with a pinned version and checksum or signature.

Risk: Write actions can submit or cancel fal.ai queued model requests.

Mitigation: Require separate user approval for fal.ai write actions, including the exact payload and expected effect, before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fal-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [fal.ai homepage](https://fal.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing data and meta.executionId fields.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
