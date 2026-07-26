## Description: <br>
Coin launch memory and verification workflow for Clawnch (4claw, Moltx, and Moltbook) that helps agents record canonical receipts, update local dashboards, and save monitoring links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to manage Clawnch token launches, preserve contract receipts, and run best-effort monitoring for STARCORE-family or similarly configured symbols. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled GitHub publishing utilities can use local GitHub credentials to create or update a public repository and push files. <br>
Mitigation: Do not run push_github_auto.py or create_github_repo.ps1 unless public repository creation and GitHub credential use are explicitly intended; review repository contents before any push. <br>
Risk: The secret-scanning utility can install or modify a local git pre-commit hook. <br>
Mitigation: Run scan_for_secrets.py only in review mode unless hook installation is intended, and inspect hook changes before relying on them. <br>
Risk: Indexer checks can lag behind Clawnch and may temporarily report missing contracts or pairs. <br>
Mitigation: Treat Clawnch receipts as authoritative and use Blockscout and Dexscreener checks as best-effort monitoring signals. <br>


## Reference(s): <br>
- [Clawnch launches API](https://clawn.ch/api/launches) <br>
- [Clanker contract pages](https://clanker.world/clanker/<contract>) <br>
- [Base Blockscout address lookup](https://base.blockscout.com/address/<contract>) <br>
- [Dexscreener contract search](https://api.dexscreener.com/latest/dex/search/?q=<contract>) <br>
- [Cron Template - STARCORE family monitor](references/cron_template_starcore_family.md) <br>
- [Cryptocurrency tools separation policy](CRYPTO_LATTICE_SEPARATION.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, markdown, JSON] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON and Markdown receipt artifacts from bundled scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides or invokes scripts that write local receipt JSON, human-readable launch summaries, bookmark entries, verification reports, and optional monitoring logs.] <br>

## Skill Version(s): <br>
1.1.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
