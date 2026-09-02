## Description:

Collect structured Indeed job-posting data from a known Indeed job URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit known Indeed job URLs to Dataify, wait for collection tasks, and return structured job-listing results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indeed URLs and collection requests are processed by Dataify as a third-party service.

Mitigation: Install and run the skill only when Dataify is acceptable as the processor for the provided URLs.

Risk: The skill requires a Dataify API token, which could be exposed if pasted into chat or logs.

Mitigation: Use a platform secret store or session-scoped environment variable for DATAIFY_API_TOKEN, and never print or paste token values into chat.

Risk: Broad, high-volume, or multi-input collection requests may consume Dataify account credits.

Mitigation: Review high-volume requests before execution and confirm scope when cost-impacting ambiguity is present.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-indeed-job-listings)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder?platform=1)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands; final collection results as JSON when task completion succeeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID and resume command if monitoring times out or no-wait behavior is requested.]

## Skill Version(s):

1.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
