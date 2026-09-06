## Description:

Collects a Facebook personal profile from a known profile URL, excluding posts, comments, events, pages, and company data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Builder jobs for known Facebook personal profile URLs, monitor the asynchronous task, and return the collected JSON result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Facebook profile URLs to Dataify and can consume Dataify account credits.

Mitigation: Install and run it only when that data transfer and credit use are intended, and review multi-profile or higher-cost collection requests before execution.

Risk: A Dataify API TOKEN could be exposed if handled directly in chat or logs.

Mitigation: Configure DATAIFY_API_TOKEN through the shell or environment, verify only that it is present, and never print the token value.

Risk: Requests outside the intended target type could collect unsupported or unwanted data.

Mitigation: Use only Facebook personal profile URLs that start with https://www.facebook.com/ and exclude posts, comments, events, pages, and company data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-facebook-profile-by-url)
- [Dataify publisher profile](https://clawhub.ai/user/dataify-server)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify API token login](https://dashboard.dataify.com/login?utm_source=skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command examples and JSON task or result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit a Dataify Builder task, monitor the returned task ID, and summarize large final payloads while preserving access to raw results.]

## Skill Version(s):

1.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
