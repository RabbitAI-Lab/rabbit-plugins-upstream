## Description:

Collect Google Play app reviews from a known Play Store app URL. Do not use for app discovery, rankings, or general Google Play search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Builder jobs for known Google Play app URLs, wait for completion, and retrieve JSON results. It is scoped to URL-based Google Play review collection, not app discovery or rankings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the release as suspicious because it includes broader Dataify workflows and weak scoping around inputs and imports.

Mitigation: Review before installing, keep use limited to the named Google Play review workflow, and avoid broad or sensitive URLs.

Risk: The workflow requires a Dataify API token.

Mitigation: Use only a token suitable for this workflow, prefer session-scoped setup, and never paste or expose the token in chat or generated output.

## Reference(s):

- [Tool parameter catalog](references/tool-params.json)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-play-store-reviews-by-url)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID and resume command when monitoring times out or no-wait behavior is requested.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
