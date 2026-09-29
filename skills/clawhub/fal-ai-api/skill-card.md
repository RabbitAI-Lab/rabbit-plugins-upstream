## Description:

Helps agents use fal.ai models through a Maton connection for image, video, and audio generation and processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to run fal.ai models for generating or processing images, video, and audio. With explicit approval, they can also connect an account and set up hosted functions or scheduled and event-driven workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account connections and model requests can access or change data through the authorized connection.

Mitigation: Confirm each new connection and write with the user; use only the permissions needed for the task.

Risk: Hosted functions and triggers can continue running and forwarding event or generated content after the initial request.

Mitigation: Require explicit approval for deployments, triggers, and destinations; limit event scope and review or remove persistent workflows when no longer needed.

Risk: Credentials or sensitive event data may be exposed through logs, configuration, or external destinations.

Mitigation: Keep credentials out of outputs and destination settings, and confirm the destination and minimum data shared before enabling forwarding.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/byungkyu/skills/fal-ai-api)
- [Maton homepage](https://maton.ai)
- [fal.ai documentation](https://fal.ai/docs)
- [fal.ai model gallery](https://fal.ai/models)
- [fal.ai queue API reference](https://fal.ai/docs/model-endpoints/queue)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples; model responses may include JSON and generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton account and fal.ai connection.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
