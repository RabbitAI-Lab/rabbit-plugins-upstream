## Description: <br>
Clawnch coin-launch receipts + local verify: pull launches from clawn.ch, write receipt JSON/MD, optional Blockscout/Dexscreener checks, local bookmark ref files. No git push, no GitHub token load, no repo create. Not for remote wallet control. Read references/SECURITY.md first. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
LYGO Sovereign License v2.0 <br>


## Use Case: <br>
Developers and operators use this skill to pull public Clawnch launch receipts, normalize STARCORE-family launch records, and verify public indexer data without handling credentials or remote wallet control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet secrets or mnemonics could be exposed if users paste them into the workspace. <br>
Mitigation: Use only public wallet or address information with this skill and keep private keys, seed phrases, and wallet files outside the skill workspace. <br>
Risk: Receipt and verification commands write local JSON or Markdown files and could clutter or overwrite expected state paths. <br>
Mitigation: Run the skill in a dedicated workspace and review output paths such as state/ and reference/ before scheduling or repeating commands. <br>
Risk: Optional monitor or cron usage performs recurring network checks and local report writes. <br>
Mitigation: Treat monitoring as manual setup, keep polling frequency low, and review generated reports before acting on them. <br>
Risk: Public indexers such as Blockscout or Dexscreener can lag behind Clawnch launch data. <br>
Mitigation: Treat Clawnch receipts as authoritative for launch records and human-review indexer verification results before relying on them. <br>


## Reference(s): <br>
- [LYRA Coin Launch Manager on ClawHub](https://clawhub.ai/deepseekoracle/skills/lyra-coin-launch-manager) <br>
- [Project homepage](https://github.com/DeepSeekOracle/lyra-crypto-operator) <br>
- [Security](references/SECURITY.md) <br>
- [SkillSpector Audit](references/SKILLSPECTOR_AUDIT.md) <br>
- [Crypto Lattice Separation](CRYPTO_LATTICE_SEPARATION.md) <br>
- [Cron Template](references/cron_template_starcore_family.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples; executed helper scripts write local JSON and Markdown receipt or verification files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Network use is limited to HTTPS GET requests for public launch and indexer data; local writes are intended for state and reference paths under the chosen workspace.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter, claw.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
