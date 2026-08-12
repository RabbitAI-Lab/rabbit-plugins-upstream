## Description:

aigate helps agents and developers use a self-hosted OpenAI-compatible AI gateway that aggregates model routing, optional AI tools, browser automation, media generation, storage, search, messaging, code execution, and a web UI behind one bearer-token endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use aigate when they want a one-command, self-hosted OpenAI-compatible endpoint that routes across local and cloud providers and exposes optional AI services without wiring each service separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single AIGATE_TOKEN can grant broad access to enabled model providers, code execution, browser automation, messaging, storage, and other services.

Mitigation: Keep AIGATE_TOKEN and service configs private, split per-service tokens where possible, enable only needed services, and give the token only to fully trusted agents for explicit user-requested actions.

Risk: Exposing the gateway on port 4000 can widen access to a high-capability local AI infrastructure service.

Mitigation: Avoid direct public exposure of port 4000; place the service behind a real authenticated access layer or a controlled private access path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate setup](references/setup.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with bash and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AIGATE_TOKEN and optional service-specific credentials supplied by the operator.]

## Skill Version(s):

3.19.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
