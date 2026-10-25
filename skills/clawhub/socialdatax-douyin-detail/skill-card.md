## Description:

Retrieves structured details and interaction metrics for Douyin works, including video and image/text posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve structured details and interaction metrics for an identified Douyin work for content research and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI dependency may be unpinned when invoked with @latest.

Mitigation: Prefer a reviewed, pinned CLI version when possible.

Risk: API use requires a SocialDataX API key and may incur charges.

Mitigation: Protect SOCIALDATAX_API_KEY and consider API charges before making requests.

Risk: The external package is not sandboxed by the skill's read-only instructions, and optional media downloads write local files.

Mitigation: Review the package before execution and choose the download directory explicitly.

## Reference(s):

- [SocialDataX API Access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub Skill Release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-detail)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON results and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns available work details and interaction metrics; optional media downloads save to a user-selected local directory.]

## Skill Version(s):

0.1.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
