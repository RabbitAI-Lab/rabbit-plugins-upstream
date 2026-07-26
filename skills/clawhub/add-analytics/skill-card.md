## Description: <br>
Add Google Analytics 4 tracking to any project. Detects framework, adds tracking code, sets up events, and configures privacy settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeftekhari](https://clawhub.ai/user/jeftekhari) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to add GA4 tracking to web projects across common frameworks, including measurement ID validation, optional event helpers, consent integration, and debug setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GA4 tracking can collect personal or sensitive data if custom events include PII, sensitive search terms, or detailed errors. <br>
Mitigation: Review generated event parameters, remove sensitive fields, and align analytics collection with the site's privacy policy. <br>
Risk: Analytics deployment may require user consent or privacy-policy updates depending on audience and jurisdiction. <br>
Mitigation: Use the consent integration where applicable and confirm local privacy requirements before release. <br>


## Reference(s): <br>
- [GA4 recommended events](https://support.google.com/analytics/answer/9267735) <br>
- [Google Analytics Debugger Chrome extension](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with framework-specific code blocks and file-change guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a GA4 Measurement ID and supports optional --events, --consent, and --debug flags.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
