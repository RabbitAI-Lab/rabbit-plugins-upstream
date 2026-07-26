## Description: <br>
Uses Warden Studio browser automation to help register and publish a Community Agent to the Warden Agent Hub with explicit confirmation gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kryptopaid](https://clawhub.ai/user/kryptopaid) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to prepare, review, publish, and verify Warden Studio Community Agent listings. It is suited for workflows that need browser-based form drafting, endpoint/auth configuration guidance, billing review, wallet approval checkpoints, and post-publish verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing or registering an agent can trigger payment and wallet-signing actions. <br>
Mitigation: Verify the official Studio URL, Base network, USDC fee, gas estimate, and wallet prompt before approving registration. <br>
Risk: Private keys, seed phrases, credentials, or API keys could be exposed if entered into chat. <br>
Mitigation: Never share seed phrases or private keys, and enter API keys only directly into the Studio UI. <br>
Risk: Incorrect endpoint, auth, billing, or fee settings can lead to failed validation or unintended publication details. <br>
Mitigation: Use read-only validation, review all submission details, and require explicit confirmation before final execution. <br>


## Reference(s): <br>
- [Warden Studio UI Notes](references/warden-studio-ui-notes.md) <br>
- [Warden Studio](https://studio.wardenprotocol.org/) <br>
- [Warden Studio Register Agent Page](https://studio.wardenprotocol.org/agents/create) <br>
- [ClawHub Skill Page](https://clawhub.ai/kryptopaid/skills/warden-studio-deploy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with browser automation steps and submission summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user approval before final publish, registration, payment, or wallet-signing actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
