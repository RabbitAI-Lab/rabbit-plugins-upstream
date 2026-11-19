## Description:

Headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research. Camoufox + OS-level input + persistent fingerprints. Use only with sites you own or have written authorization to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security testers use this skill to automate browser based QA, compatibility checks, and defensive research on sites they own or are explicitly authorized to test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Docker `latest` image can change between pulls, and the supplied scan had partial coverage because some local references could not be resolved.

Mitigation: Review unresolved local references and pin a reviewed image digest; limit the container's file and network access and use isolated test credentials.

Risk: An instance without API authentication or an exposed noVNC viewer can allow others who can reach it to control the browser and access its session data.

Mitigation: Bind the API and viewer to loopback, set `AUTH_TOKEN` for non-trivial deployments, and do not publish the viewer beyond localhost.

Risk: Browser automation, persistent profiles, page loaders, and automatic dialog acceptance can expose sensitive data or trigger state changes; use against unauthorized sites can cause harm.

Mitigation: Use only owned or explicitly authorized targets, test accounts, and audited loaders; scope captured data, protect profile volumes, and disable dialog auto-accept before stateful actions.

## Reference(s):

- [Setup and security guidance](references/setup.md)
- [Humanized input API documentation](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)
- [Script mode control flow documentation](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)
- [Project homepage](https://github.com/psyb0t/docker-stealthy-auto-browse)

## Skill Output:

**Output Type(s):** [Text, HTML, JSON, Screenshots, Files]

**Output Format:** [Browser interaction results and captured page content, including structured JSON, text, HTML, screenshots, downloads, and recordings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected browser action and authorized target; text extraction is bounded, and captured files may contain sensitive session or page data.]

## Skill Version(s):

3.8.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
