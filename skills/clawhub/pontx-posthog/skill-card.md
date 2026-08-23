## Description:

Use for PostHog project-token runtime capture, event batching, and remote feature-flag evaluation with caller-owned tokens, local previews, and explicit confirmation before any provider request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate PostHog runtime event capture, event batching, and remote feature-flag evaluation while keeping project tokens local and requiring reviewed previews before provider requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PostHog project tokens could be exposed if copied into source, logs, terminal history, Hub, or chat.

Mitigation: Keep tokens in local environment variables or client options, and review local previews without disclosing token values.

Risk: Event capture and feature-flag evaluation can write analytics data, affect quota, or target the wrong PostHog environment.

Mitigation: Confirm only reviewed requests that target the intended project and environment, and create a fresh preview whenever inputs change.

Risk: Batch or backfill requests can send unintended event, person, or group data at larger scope.

Mitigation: Prefer single capture for one deliberate event and use batch capture only after every entry and batch scope has been bounded and reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pontjs/skills/pontx-posthog)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local preview and confirmation guidance for caller-directed PostHog runtime requests.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
