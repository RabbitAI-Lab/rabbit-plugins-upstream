## Description:

Generate short 16:9 AI videos with Kling 2.6 through the Kie.ai API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alti-systems](https://clawhub.ai/user/alti-systems)

### License/Terms of Use:


## Use Case:

Marketing teams, fitness businesses, and developers use this skill to create short promotional, UGC-style, testimonial, LinkedIn, and product-demo videos from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation settings are sent to Kie.ai.

Mitigation: Avoid confidential, regulated, or sensitive prompt content unless that third-party processing is approved.

Risk: The security evidence reports a vulnerable authenticated HTTP client stack.

Mitigation: Update or pin the HTTP dependencies to reviewed safe versions before using a KIE_API_KEY.

Risk: The skill requires an API key for authenticated requests.

Mitigation: Use scoped credentials where available and avoid sharing or committing KIE_API_KEY values.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [CLI text and JSON containing task IDs, status data, credit data, and generated video URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires KIE_API_KEY; video generation may take 1-5 minutes.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
