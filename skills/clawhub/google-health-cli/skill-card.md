## Description: <br>
Google Health lets agents authenticate with read-only OAuth2, list Google Health data points, fetch daily roll-ups and exercise sessions, and emit the results as JSON for downstream parsing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stozo04](https://clawhub.ai/user/stozo04) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and external agent users use this skill to connect an agent to their own Google Health account, retrieve read-only health and fitness data, and parse JSON results in the calling workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth client secrets and cached tokens are sensitive local credentials, and the security summary notes that setup guidance under-explains protecting a locally stored client secret. <br>
Mitigation: Keep config.json and token caches out of source control and untrusted backups, restrict them to the user account, and rotate the OAuth client secret if exposure is suspected. <br>
Risk: Health data emitted on stdout can be logged, persisted, summarized, or transmitted by an agent or pipeline. <br>
Mitigation: Run only in trusted contexts, request the narrowest useful data type and time window, and avoid retaining or forwarding output beyond the task. <br>
Risk: Raw read-only API access can expose broader personal data such as profile or settings endpoints. <br>
Mitigation: Prefer typed data, roll-up, and sessions commands, and use raw API GET only when a typed command cannot answer the request. <br>


## Reference(s): <br>
- [Google Health CLI homepage](https://github.com/stozo04/google-health-cli) <br>
- [OAuth setup guide](artifact/OAUTH_SETUP.md) <br>
- [Agent machine contract](artifact/AGENTS.md) <br>
- [Google Health API](https://health.googleapis.com) <br>
- [ClawHub skill page](https://clawhub.ai/stozo04/skills/google-health-cli) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON on stdout with stderr hints, plus Markdown setup and command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses read-only Google Health scopes; data output can contain sensitive health, profile, settings, and local environment information.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
