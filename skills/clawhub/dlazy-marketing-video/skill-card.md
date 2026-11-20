## Description:

Creates marketing, promotional, or advertising videos from a product, brand, or brief for social media or campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers and ecommerce sellers use this skill to create promotional shopping videos from product information, listings, or a campaign brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to dLazy's hosted service, and attached files are uploaded to its media storage.

Mitigation: Only submit material approved for that service; avoid sharing sensitive or confidential content.

Risk: The documented workflow includes CLI authentication and organization project listing; the security review says their relationship to video creation is unclear and its analysis is partial.

Mitigation: Review the CLI behavior before signing in or listing projects, and keep the API key private; rotate or revoke it if exposed.

Risk: Server-resolved GitHub provenance is unavailable, although the skill metadata lists a repository link.

Mitigation: Treat that repository as an unverified reference and review the CLI package and repository before installation.

## Reference(s):

- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text]

**Output Format:** [Generated marketing video with streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation runs through dLazy's hosted service; attached reference files are uploaded for processing.]

## Skill Version(s):

1.0.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
