## Description:

Guides developers in setting up and using a self-hosted, OpenAI-compatible gateway for model routing and optional AI tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to deploy and operate a self-hosted AI gateway, route requests across local and cloud models, and selectively enable tools such as search, browser automation, and code execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single gateway token can grant broad access to enabled host, browser, messaging, and storage services.

Mitigation: Set strong, separate per-service tokens before granting agent access; give the master token only to fully trusted agents for explicitly requested actions.

Risk: Exposing the gateway publicly can make its powerful services accessible to unauthorized users.

Mitigation: Keep the gateway local or behind an authenticated tunnel, and enable only the services needed.

## Reference(s):

- [aigate on ClawHub](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate setup guide](references/setup.md)
- [Project homepage listed by the skill](https://github.com/psyb0t/aigate)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment and API guidance depends on the services the operator enables.]

## Skill Version(s):

9.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
