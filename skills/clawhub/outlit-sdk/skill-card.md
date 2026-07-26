## Description: <br>
Use when integrating Outlit tracking into web, server, native, or desktop apps; adding SDK event tracking, identity, consent, activation configuration, billing integrations, visitor tracking, customerId attribution, or troubleshooting @outlit/browser, @outlit/node, or the Rust outlit crate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leo-paz](https://clawhub.ai/user/leo-paz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add or troubleshoot Outlit analytics across browser, server, native, and desktop applications while preserving existing application structure. It guides SDK choice, identity mapping, consent handling, event tracking, activation setup, billing integration, and verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser auto-tracking can create visitor storage and link activity to email, name, user ID, customer ID, or device fingerprint before consent and privacy requirements are confirmed. <br>
Mitigation: Confirm consent, privacy notice, and data-processing requirements before enabling tracking; when consent is required, initialize with autoTrack disabled and enable tracking only from the consent flow. <br>
Risk: Server or native events may be dropped or unattributed if required identity fields are missing or queued events are not flushed before exit. <br>
Mitigation: Provide at least one supported identifier for server track calls and flush or shut down the SDK client before serverless handlers or processes exit. <br>
Risk: Billing or lifecycle status can be misrepresented if custom SDK events are treated as authoritative account state. <br>
Mitigation: Use verified billing integrations for billing status and reserve SDK events for identity and ordinary product activity. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/leo-paz/skills/outlit-sdk) <br>
- [Outlit Tracking Quickstart](https://docs.outlit.ai/tracking/quickstart) <br>
- [Outlit Browser SDK](https://docs.outlit.ai/tracking/browser/npm) <br>
- [Outlit React Tracking](https://docs.outlit.ai/tracking/browser/react) <br>
- [Outlit Node.js Tracking](https://docs.outlit.ai/tracking/server/nodejs) <br>
- [Outlit Rust and Tauri Tracking](https://docs.outlit.ai/tracking/server/rust) <br>
- [Outlit Identity Resolution](https://docs.outlit.ai/concepts/identity-resolution) <br>
- [Outlit Website Visitors](https://docs.outlit.ai/concepts/website-visitors) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline code blocks and implementation steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask for an Outlit public key, framework details, consent requirements, or activation-event confirmation before changing code.] <br>

## Skill Version(s): <br>
1.0.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
