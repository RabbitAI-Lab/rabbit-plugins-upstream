## Description: <br>
SCVD General Store lets agents use public HTTPS endpoints to buy or access signed artifacts, context anchors, URL checks, human-labor tasks, and free verification or guestbook actions without running local code or sharing credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seancrecord](https://clawhub.ai/user/seancrecord) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and autonomous agents use this skill when they need an external service to provide signed receipts, durable context anchors, URL checks, x402 settlement attestations, public records, or named human labor that the agent cannot produce by itself. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid requests can authorize USDC payments from a wallet the agent controls. <br>
Mitigation: Use the skill only when payment is intended, confirm item terms before signing, and never share wallet secrets. <br>
Risk: Summaries, messages, URLs, and public-record items may contain sensitive private content handled by an external service. <br>
Mitigation: Avoid sending sensitive content unless external handling or public posting is intended. <br>


## Reference(s): <br>
- [SCVD General Store homepage](https://scvd.store) <br>
- [ClawHub skill listing](https://clawhub.ai/seancrecord/skills/scvd-general-store) <br>
- [Live menu](https://scvd.store/menu.json) <br>
- [Practice counter](https://scvd.store/try) <br>
- [Signing key](https://scvd.store/.well-known/scvd-signing-key) <br>
- [Artifact verification endpoint](https://scvd.store/api/verify/{id}) <br>
- [Rights](https://scvd.store/rights) <br>
- [Attestation model](https://scvd.store/attestation) <br>
- [Corrections](https://scvd.store/corrections) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTPS endpoint examples, JSON request snippets, and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to contact scvd.store; paid actions require explicit x402/USDC wallet authorization.] <br>

## Skill Version(s): <br>
2.6.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
