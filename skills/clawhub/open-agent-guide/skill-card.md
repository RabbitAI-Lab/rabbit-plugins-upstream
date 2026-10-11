## Description:

Guides agents through reading and contributing to the Open Agent Guide public catalog, including signup, API authentication, catalog endpoints, and submission workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twschiller](https://clawhub.ai/user/twschiller)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to search the public Open Agent Guide catalog and prepare or submit sourced changes to catalog records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed API token could permit unauthorized authenticated catalog actions.

Mitigation: Keep OAG_TOKEN private and use it only for intended authenticated requests.

Risk: Submitted catalog information may become public.

Mitigation: Review and cite proposed changes, and submit only information intended for the public catalog.

Risk: An untrusted API base URL could receive credentials or submissions.

Mitigation: Keep the default OAG_BASE_URL unless the alternative service is trusted.

## Reference(s):

- [Open Agent Guide API reference](artifact/references/api-reference.md)
- [Open Agent Guide onboarding](artifact/references/onboarding.md)
- [Batch submission guidance](artifact/references/batch-populating.md)
- [Open Agent Guide live API specification](https://www.openagentguide.com/api/v1/openapi.json)
- [ClawHub skill release](https://clawhub.ai/twschiller/skills/open-agent-guide)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
