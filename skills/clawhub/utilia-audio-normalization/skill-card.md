## Description: <br>
Normalize a public HTTPS audio file to a bounded 128 kbps MP3 with measured loudness, duration, and SHA-256 evidence through Utilia's wallet-funded x402 service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohamedkuch](https://clawhub.ai/user/mohamedkuch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to normalize user-approved public HTTPS audio for podcasts, voice notes, transcription preparation, and consistent agent-generated audio. It helps produce a local bounded MP3 while returning loudness, duration, and SHA-256 evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid calls spend Solana USDC through a third-party service. <br>
Mitigation: Use a dedicated low-balance Solana USDC wallet and approve each paid call deliberately. <br>
Risk: Audio URLs and related request metadata are shared with Utilia. <br>
Mitigation: Submit only public HTTPS audio URLs that the user has approved and is comfortable sharing with Utilia. <br>
Risk: Private key exposure would compromise the payment wallet. <br>
Mitigation: Do not paste private keys into chat; configure credentials only through the local environment or keypair path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohamedkuch/skills/utilia-audio-normalization) <br>
- [Utilia MCP endpoint](https://api.utilia.ink/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and local MP3 file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns the absolute output path with reported input/output loudness, duration, byte-count, and SHA-256 evidence when normalization succeeds.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
