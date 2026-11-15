## Description:

Provides Docker-based, headless-detection-resistant browser automation for authorized QA, compatibility testing, and defensive security research on sites you own or have written authorization to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security QA teams use this browser automation skill to test their own sites or explicitly authorized targets against anti-bot systems, validate compatibility, and conduct defensive research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security assessment is suspicious and cites a broad container capability, mutable image references, and incomplete reference analysis.

Mitigation: Review the security assessment and resolve the incomplete references before installation; inspect and pin the container image used for deployment.

Risk: Persistent browser profiles can retain session cookies and other sensitive account data.

Mitigation: Use dedicated test accounts, protect profile data as a secret, and remove the profile when testing is complete.

Risk: An API instance without authentication gives anyone who can reach it browser control.

Mitigation: Bind the service to loopback and configure AUTH_TOKEN or an authenticating proxy before allowing network access.

## Reference(s):

- [Setup](references/setup.md)
- [Humanized Input API](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)
- [Script Mode Control Flow](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)

## Skill Output:

**Output Type(s):** [Text, JSON, Images, Video files]

**Output Format:** [Structured JSON responses, page text or HTML, screenshots, and recordings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested browser action and authorized test scope.]

## Skill Version(s):

3.5.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
