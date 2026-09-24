## Description:

Provides Taizhou scenic-spot heat rankings and recent visitor and overnight-stay trends for tourism operations and cultural-tourism analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External tourism and cultural-tourism teams use this skill to retrieve Taizhou scenic-area popularity rankings, 30-day trend data, and related visitor signals for staffing, stocking, marketing, and traffic analysis decisions.

### Deployment Geography for Use:

China (Taizhou, Zhejiang data coverage)

## Known Risks and Mitigations:

Risk: The skill contacts an external service for live data.

Mitigation: Use it only when the publisher and external endpoint are trusted, and review network access expectations before installation.

Risk: The skill may create a plaintext credential and session file in the user's home directory and send product API keys, cookies, or an install identifier back to the service for quota or paid access checks.

Mitigation: Use dedicated product credentials, avoid sharing the local credential file, and remove stored credentials when access is no longer needed.

Risk: Security evidence marks the release as suspicious because local credential and cookie storage is not clearly disclosed to users.

Mitigation: Disclose credential/session storage before use and require users to consent to the local storage and transmission behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/taizhou-scenic-heat-board)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text summaries with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns live data from an external service when network access and any required product credentials are available.]

## Skill Version(s):

1.0.21 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
