## Description:

Guides an agent in creating a minimal static OpenClaw runner page where users provide an API key, base URL, and model, with streamed or polled output after Gateway endpoints are confirmed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to scaffold or specify a lightweight browser-based OpenClaw agent runner without adding a backend. It is intended for workflows where the user supplies Gateway connection details and confirms the exact REST or WebSocket endpoints before live execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can be exposed if stored in browser localStorage or rendered into logs, DOM text, or unexpected network requests.

Mitigation: Keep API keys memory-only by default, make localStorage strictly opt-in with a warning, use password inputs, and send credentials only to the user-specified Base URL.

Risk: OpenClaw Gateway REST or WebSocket endpoints may differ across deployments or versions.

Mitigation: Confirm the exact Gateway endpoints with the running instance before enabling real run or streaming calls, and validate with a harmless request first.

Risk: Browser CORS or authentication failures can prevent the generated page from reaching the Gateway.

Mitigation: Detect failures and show clear user-facing errors, then configure Gateway CORS or use a small trusted proxy where appropriate.

Risk: The scaffold script provides a dry-run UI stub and does not itself implement live agent execution.

Mitigation: Treat generated files as a starting point and review the completed Gateway integration before presenting the page as a working runner.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/agent-runner-site)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance and generated static site files such as HTML, CSS, and JavaScript]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled scaffold script creates local static-site files and leaves Gateway REST/WebSocket integration as a verified implementation step.]

## Skill Version(s):

1.0.0 (source: release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
