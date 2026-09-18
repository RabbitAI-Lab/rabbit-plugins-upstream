## Description:

APIpie AI lets agents inspect connector schemas and run APIpie AI chat completion, embedding, and model-listing actions through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to interact with APIpie AI through the OOMOL connector, including chat completions, embeddings, and model discovery. It is suited to tasks where the agent should inspect the live action schema before sending JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts for the oo CLI.

Mitigation: Review or replace the CLI setup path with an official, pinned, and verifiable installation method before installing.

Risk: Chat completion and embedding actions are write actions that may create usage costs or unintended API activity.

Mitigation: Confirm the exact payload, intended effect, and potential cost with the user before running write actions.

## Reference(s):

- [APIpie AI homepage](https://apipie.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apipie-ai)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
