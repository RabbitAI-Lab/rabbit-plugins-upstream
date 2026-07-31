## Description: <br>
Create text-to-speech narration and MP3 audio with UnlimitedTTS using x402 USDC payments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sisygoboom](https://clawhub.ai/user/sisygoboom) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to create paid text-to-speech narration and MP3 audio through UnlimitedTTS while checking quotes, payment settlement, voice selection, and wallet-safety constraints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate paid speech generation when paired with MCP or wallet tools. <br>
Mitigation: Check the quoted USDC amount, payee, Base network requirement, voice, text, speed, and user budget before approving any payment signature. <br>
Risk: Wallet secrets could be exposed if an agent asks for private keys or seed phrases. <br>
Mitigation: Use a wallet-aware signing tool and never provide private keys, seed phrases, or wallet secrets in chat, tool arguments, source code, or logs. <br>
Risk: Retrying an ambiguous payment outcome can cause duplicate payment authorization. <br>
Mitigation: Do not retry payment-outcome-unknown cases; inspect the wallet, settlement receipt, facilitator, or chain state before requesting a new quote or authorization. <br>


## Reference(s): <br>
- [UnlimitedTTS Skill on ClawHub](https://clawhub.ai/sisygoboom/skills/unlimitedtts-skill) <br>
- [Server-resolved GitHub source](https://github.com/sisygoboom/unlimitedtts-agents/tree/main/packages/openclaw/skills/unlimitedtts) <br>
- [Direct x402 mode](references/direct-x402.md) <br>
- [Error recovery](references/errors.md) <br>
- [UnlimitedTTS API docs](https://api.unlimitedtts.com/docs) <br>
- [UnlimitedTTS voice list](https://api.unlimitedtts.com/tts/voices) <br>
- [UnlimitedTTS x402 TTS endpoint](https://api.unlimitedtts.com/x402/tts) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, files, guidance] <br>
**Output Format:** [Markdown guidance with tool or HTTP call instructions; successful synthesis returns an MP3 audio attachment or resource.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires quote review, user payment approval, wallet signing, and settled payment confirmation before returning audio.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
