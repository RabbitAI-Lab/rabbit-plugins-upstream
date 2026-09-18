## Description:

A flight fare comparison and purchase-timing assistant for domestic China routes that searches live prices, scans low-fare dates, and emits buy, wait, or monitor guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel agents use this skill to compare domestic flight prices, identify lower-fare travel dates, and receive purchase-timing guidance before booking on a travel platform. Host agents can also use it to create monitor task requests for later price checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release contains a shared proxy token while its documentation says credentials are read from an environment variable.

Mitigation: Rotate the shared token, remove the hard-coded value, and load credentials from an environment variable or managed secret before wider use.

Risk: Route and travel-date queries are sent to third-party proxy services for live flight data.

Mitigation: Disclose the data flow to users, avoid sending unnecessary personal data, and review the proxy service controls before installation.

Risk: Purchase-timing and multi-platform comparison claims may be overstated for volatile flight prices.

Mitigation: Treat output as decision support, verify prices on the booking platform, and correct the public claims before users rely on them for purchases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/smart-flight-buy)
- [Skill homepage](https://rollinggo.store)

## Skill Output:

**Output Type(s):** [text, json, guidance, configuration]

**Output Format:** [JSON objects with concise user-facing travel guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search returns up to 20 flights; calendar scans up to 30 days; monitor emits a task request for a host agent.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
