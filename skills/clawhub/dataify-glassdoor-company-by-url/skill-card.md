## Description:

Collect structured Glassdoor company information from one or more known company URLs. Do not use for job-search results or Indeed company URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit known Glassdoor company URLs to Dataify, monitor the asynchronous collection task, and receive the final structured JSON result. It is scoped to Glassdoor company-by-URL collection and should not be used for job-search results or Indeed company URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataify receives submitted targets and uses the caller's API token during collection.

Mitigation: Install only if the publisher is trusted, submit only targets appropriate for Dataify processing, keep the token in the environment, and rotate it if it may have appeared in logs.

Risk: The artifact reaches beyond the advertised company-URL scope with job-listing and generic workflow support.

Mitigation: Restrict use to glassdoor_company_by-url before deployment, or remove and isolate broader job-listing and generic workflow scripts.

Risk: Persistent token setup can expose credentials if copied into shared shell profiles or logs.

Mitigation: Prefer least-exposed environment configuration, never paste the token into chat, and verify only that DATAIFY_API_TOKEN is present.

## Reference(s):

- [Tool parameter catalog](references/tool-params.json)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-glassdoor-company-by-url)
- [Dataify Builder API endpoint](https://scraperapi.dataify.com/builder)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON result payloads with optional Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DATAIFY_API_TOKEN from the environment; default completion waits for the asynchronous task and returns a resume command rather than resubmitting timed-out work.]

## Skill Version(s):

1.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
