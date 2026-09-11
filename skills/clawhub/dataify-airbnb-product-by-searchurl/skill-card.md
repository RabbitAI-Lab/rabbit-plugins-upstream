## Description:

Collect structured Airbnb listing results from a known Airbnb search-results URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Airbnb search targets to Dataify, monitor the asynchronous task, and retrieve structured listing results. It is intended for known Airbnb search-results URLs, not general hotel discovery or Booking.com scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataify receives the Airbnb target data and may consume account credits for successful requests.

Mitigation: Use the skill only for intended Airbnb targets, confirm high-volume scope before execution, and monitor Dataify account credit usage.

Risk: Credential handling weaknesses may expose the Dataify API key in request URLs or logs.

Mitigation: Keep DATAIFY_API_TOKEN in the environment, never paste it into chat, avoid logging request URLs that contain credentials, and rotate the token if exposure is suspected.

Risk: The package includes broader scraping helpers and under-scoped execution paths beyond the Airbnb Builder workflow.

Mitigation: Review the package before installation and restrict execution to the documented Airbnb collection workflow and required helper scripts.

## Reference(s):

- [Tool parameter catalog](artifact/references/tool-params.json)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-airbnb-product-by-searchurl)
- [Dataify publisher profile](https://clawhub.ai/user/dataify-server)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration guidance]

**Output Format:** [JSON results, with curl commands or setup guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN; default task wait is 600 seconds, with resume guidance on timeout or interruption.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
