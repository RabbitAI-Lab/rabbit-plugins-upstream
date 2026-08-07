## Description: <br>
PulseFeed helps agents check x402 payment endpoints and npm/MCP packages before paying or installing by surfacing liveness, trust, package risk, and incident signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nikolife2016](https://clawhub.ai/user/nikolife2016) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill before paying x402/USDC endpoints or installing MCP/npm packages, especially when a target is unknown or needs a current trust check. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on a third-party PulseFeed service for pre-payment and pre-install checks. <br>
Mitigation: Treat PulseFeed results as decision support, review returned verdicts and flags, and avoid acting on results you cannot inspect or accept. <br>
Risk: The optional live deep check uses x402 payment and may spend USDC. <br>
Mitigation: Review the payment challenge, endpoint, receiver, and amount before paying, and set an explicit client-side payment cap. <br>
Risk: The referenced MCP server, guard SDK, or package checks can lead to installing third-party code. <br>
Mitigation: Verify package results first, review install-script, repository, license, abandonment, and provenance flags, and install only when those findings are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nikolife2016/skills/pulsefeed-x402-trust) <br>
- [PulseFeed methodology](https://pulsefeed.dev/methodology) <br>
- [PulseFeed incidents feed](https://pulsefeed.dev/incidents.json) <br>
- [PulseFeed status API](https://pulsefeed.dev/status.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with curl commands, JSON response descriptions, and JavaScript snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include links to PulseFeed endpoints and recommendations to review returned verdicts, flags, scores, provenance, and receiver data before acting.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
