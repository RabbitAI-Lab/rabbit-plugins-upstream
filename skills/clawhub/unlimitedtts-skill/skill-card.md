## Description: <br>
Create text-to-speech narration and MP3 audio with UnlimitedTTS using x402 USDC payments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unlimitedtts](https://clawhub.ai/user/unlimitedtts) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to create paid text-to-speech narration or MP3 audio through UnlimitedTTS while keeping wallet secrets out of the agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text-to-speech synthesis can spend USDC and may be irreversible after settlement. <br>
Mitigation: Use a trusted wallet tool, verify the quote amount and payee, set a budget, and require explicit approval before signing. <br>
Risk: Ambiguous payment outcomes or retries can lead to duplicate authorization or payment. <br>
Mitigation: Do not automatically retry after PAYMENT_OUTCOME_UNKNOWN, timeouts, missing receipts, or ambiguous responses; inspect wallet or settlement records before any new quote or authorization. <br>
Risk: Long text may need multiple chunks, and each chunk is a separate paid request. <br>
Mitigation: Split only when needed and get approval for the aggregate cost plan before synthesizing multiple chunks. <br>
Risk: Wallet secrets could be exposed if requested through chat, tool arguments, source code, or logs. <br>
Mitigation: Never request seed phrases, private keys, or wallet secrets; ask an external wallet tool to sign only the selected payment requirement. <br>


## Reference(s): <br>
- [UnlimitedTTS Skill Page](https://clawhub.ai/unlimitedtts/skills/unlimitedtts-skill) <br>
- [Direct x402 mode](references/direct-x402.md) <br>
- [Error recovery](references/errors.md) <br>
- [UnlimitedTTS API Documentation](https://api.unlimitedtts.com/docs) <br>
- [UnlimitedTTS Voices](https://api.unlimitedtts.com/tts/voices) <br>
- [UnlimitedTTS x402 TTS Endpoint](https://api.unlimitedtts.com/x402/tts) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with API call details and MP3 audio attachment or resource output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit quote review, wallet authorization, settlement confirmation, and an audio/mpeg response before returning MP3 output.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
