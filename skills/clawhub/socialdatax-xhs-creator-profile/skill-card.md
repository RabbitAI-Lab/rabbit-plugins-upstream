## Description:

This skill retrieves Xiaohongshu (XHS/RedNote) creator profile information, including account details, creator positioning, and follower scale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts, marketers, and researchers use this skill to look up Xiaohongshu creator profile facts, such as account details and audience size. It can retrieve a profile by creator ID or profile link and report available fields separately from strategic interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key could be exposed through prompts, logs, or other local files.

Mitigation: Keep SOCIALDATAX_API_KEY in protected environment configuration and do not include its value in prompts or logs.

Risk: The external package can change between runs, and its documented read-only behavior does not technically limit local permissions.

Mitigation: Use a reviewed fixed package version and inspect it before execution; limit its local permissions to what the task needs.

Risk: Profile queries use an external service and may consume paid credits.

Mitigation: Check expected usage and available credits before running repeated or broad profile lookups.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON profile data with a concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available fields depend on the profile data returned by the external service.]

## Skill Version(s):

0.1.17 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
