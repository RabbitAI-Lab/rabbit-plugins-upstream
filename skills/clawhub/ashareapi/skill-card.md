## Description:

Guides agents in retrieving and interpreting A-share market, financial, and economic data through ashareapi's REST API and Python or Node.js SDKs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ashareapi](https://clawhub.ai/user/ashareapi)

### License/Terms of Use:

MIT

## Use Case:

Developers and other external users use this skill to help agents select A-share data endpoints, interpret response fields and dates, handle errors and rate limits, and draft API or SDK calls. It provides data-access guidance, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the remote skill ZIP globally without checking its contents could expose all projects to unreviewed files.

Mitigation: Inspect the ZIP before global installation or install the skill in a project-scoped skills directory.

Risk: Hardcoded paid API keys in generated examples or projects could be disclosed.

Mitigation: Keep API keys in environment variables rather than embedding them in examples or source files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ashareapi/skills/ashareapi)
- [ashareapi documentation](https://ashareapi.com/docs)
- [ashareapi endpoint list](https://ashareapi.com/endpoints)
- [ashareapi changelog](https://ashareapi.com/changelog)
- [Endpoint reference](references/endpoints.md)
- [Field and unit reference](references/fields.md)
- [Error and rate-limit reference](references/errors.md)
- [SDK reference](references/sdk.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with optional code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains API response shapes, units, trading dates, authentication, and rate limits; live data requires access to the external service.]

## Skill Version(s):

0.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
