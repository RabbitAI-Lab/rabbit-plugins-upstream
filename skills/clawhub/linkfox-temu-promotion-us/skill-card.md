## Description:

Provides agent workflows and Python scripts for Temu US promotion management through LinkFox, including promotion activity lookup, candidate goods lookup, enrollment, operation status checks, enrolled goods queries, goods updates, and signed file downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to work with Temu US Partner Promotion APIs through LinkFox for promotion discovery, item enrollment, status checks, and promotion goods updates.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill can call broad LinkFox and Temu proxy workflows, including promotion enrollment, update, and deactivation operations.

Mitigation: Install it only when those workflows are needed and manually confirm every action that changes promotion participation, pricing, quantity, or item status.

Risk: Temu access tokens may be supplied inline or saved locally for later use.

Mitigation: Use a dedicated least-privilege Temu token where possible, avoid passing secrets inline in shell history, and remove saved tokens when they are no longer needed.

Risk: Full API responses are saved to local linkfox session data files and may contain store or promotion data.

Mitigation: Review where response files are written and periodically delete saved response data that is no longer needed.

Risk: Gateway URL environment overrides can redirect requests away from the default LinkFox endpoint.

Mitigation: Do not set gateway override environment variables unless the endpoint is controlled and trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-promotion-us)
- [API Reference](references/api.md)
- [Partner US Promotion Catalog](references/partner-us-catalog.md)
- [Temu Access Token Guide](references/access-token.md)
- [Authorization and Billing Onboarding](references/onboarding.md)
- [Promotion API Documentation Index](references/apis/README.md)
- [Temu Partner US Promotion Documentation](https://partner-us.temu.com/documentation?menu_code=873ac072a78249c893e5f8d0e656a11f)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request or response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses under a linkfox session data directory and print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
