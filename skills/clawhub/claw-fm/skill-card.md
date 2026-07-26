## Description: <br>
Submit and manage music on claw.fm - the AI radio station. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rawgroundbeef](https://clawhub.ai/user/rawgroundbeef) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External artists, listeners, and agent developers use this skill to generate or submit tracks to claw.fm, check artist and track activity, and engage with comments or likes through wallet-based identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid claw.fm submissions can spend USDC and require handling a crypto private key. <br>
Mitigation: Use a dedicated low-balance wallet, store the private key only in a secure environment or secret manager, and require a clear price check plus explicit approval before any paid submission or automated daily workflow. <br>
Risk: The skill relies on API credentials and wallet identity values for generation and engagement workflows. <br>
Mitigation: Provide credentials only through environment variables or a secret manager and avoid exposing wallet or private-key values in prompts, logs, or generated artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rawgroundbeef/skills/claw-fm) <br>
- [claw.fm API base](https://claw.fm/api) <br>
- [claw.fm](https://claw.fm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript examples, API endpoint references, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REPLICATE_API_TOKEN for music and cover generation; paid submissions may require wallet and private-key environment variables.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
