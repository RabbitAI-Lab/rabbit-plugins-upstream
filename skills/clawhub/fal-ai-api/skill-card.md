## Description:

fal.ai API integration with managed API key authentication for running fal.ai models for image generation, video generation, audio processing, upscaling, transcription, and related AI tasks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run fal.ai queue API model jobs through a Maton-managed connection, including submitting image, video, audio, and text-to-speech requests and polling for results. It also provides guarded guidance for connection setup, authenticated calls, and optional user-approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on Maton-managed fal.ai access, so users may expose account data or long-lived credentials if they bypass the documented OAuth and credential-handling flow.

Mitigation: Use OAuth where possible, keep credentials in the operating system credential store, avoid printing or persisting API keys, and confirm comfort with Maton as the fal.ai gateway before installation.

Risk: Write operations, connection creation, function deployment, trigger destinations, webhooks, and local --exec watches can create persistent or unattended automation.

Mitigation: Require explicit user approval with the target account, data, URL, schedule, persistence, and intended effect before enabling these features; prefer read/list calls and polling when sufficient.

Risk: Generated media requests and callback URLs may disclose prompts, result URLs, or user data to external services.

Mitigation: Use only user-approved callback destinations, avoid public inspection or request-bin services, and extract only the response fields needed for the task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/fal-ai-api)
- [Maton Homepage](https://maton.ai)
- [fal.ai Documentation](https://fal.ai/docs)
- [fal.ai Model Gallery](https://fal.ai/models)
- [fal.ai Queue API Reference](https://fal.ai/docs/model-endpoints/queue)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated API call plans and response-handling guidance; model outputs are returned by fal.ai through the user's connected account.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
