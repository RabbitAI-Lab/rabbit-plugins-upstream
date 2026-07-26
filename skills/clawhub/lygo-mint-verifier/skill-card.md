## Description: <br>
LYGO-MINT Verifier canonicalizes Champion and alignment prompt packs, generates deterministic SHA-256 hashes, writes ledger receipts, and emits portable Anchor Snippets for public anchoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to mint verifiable prompt or workflow packs by producing canonical hashes, ledger receipts, and anchor snippets. It is intended for non-secret packs where public or shared verification records are useful. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill invokes local tools/lygo_mint scripts that are outside the published bundle and run with local workspace permissions. <br>
Mitigation: Inspect those local scripts before use and run the skill only in a controlled workspace. <br>
Risk: Minting or anchoring sensitive pack content could expose secrets through ledger records or public anchor snippets. <br>
Mitigation: Use non-secret prompt packs and remove private keys, API keys, or other sensitive data before minting or posting anchors. <br>


## Reference(s): <br>
- [LYGO-MINT Verifier Process](artifact/references/process.md) <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-mint-verifier) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files] <br>
**Output Format:** [Markdown/text anchor snippets plus JSON and JSONL ledger files from local Python commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes append-only and canonical ledger state under state/lygo_mint_ledger.jsonl and state/lygo_mint_ledger_canonical.json.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
