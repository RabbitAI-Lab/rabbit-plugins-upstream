## Description:

Audit a browser fingerprint for internal contradictions with the liarjs CLI across browser probes and the TLS, HTTP, and ASN view of the same request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liarjsdev](https://clawhub.ai/user/liarjsdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to run and interpret browser fingerprint audits, compare browser profile consistency, and understand which canvas, WebGL, WebGPU, audio, font, WebRTC, timezone, and network-layer checks failed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default network comparison sends one browser request to liarjs.dev, exposing IP, ASN, headers, and TLS/HTTP details for that request.

Mitigation: Use --offline when outbound comparison is not needed, or use --endpoint to point the scan at an owned deployment.

Risk: Using --cdp can interact with an already-running browser session and read page state from that session.

Mitigation: Use --cdp only when the user explicitly asks to scan that running browser, and identify the endpoint before attaching.

## Reference(s):

- [Browser Fingerprint Audit skill page](https://clawhub.ai/liarjsdev/skills/browser-fingerprint-audit)
- [checks.md](references/checks.md)
- [liarjs hosted audit](https://liarjs.dev)
- [liarjs CLI field notes](https://liarjs.dev/cli/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash commands and concise audit interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include score summaries, failed check IDs, browser setup notes, offline mode guidance, and CDP attachment cautions.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
