## Description:

Deploys a self-hosted OpenAI-compatible AI platform that routes requests across cloud and local model providers and exposes optional tools through one endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers can deploy one self-hosted endpoint for OpenAI-compatible model access, provider routing, and optional AI tools without configuring each service separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The master token can authorize code execution and account actions when those services are enabled.

Mitigation: Protect credentials, enable only needed services, and use separate service credentials when narrower access is required.

Risk: Enabled cloud providers and fallback routes may receive requests.

Mitigation: Enable only providers you intend to use and review the upstream version before deployment.

Risk: A publicly exposed gateway increases the impact of privileged services.

Mitigation: Keep the gateway private and consider running it on a dedicated machine or VM.

## Reference(s):

- [Setup guide](references/setup.md)
- [Project homepage](https://github.com/psyb0t/aigate)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/aigate)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with shell commands, configuration examples, and API usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment and service options depend on enabled components and configured credentials.]

## Skill Version(s):

12.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
