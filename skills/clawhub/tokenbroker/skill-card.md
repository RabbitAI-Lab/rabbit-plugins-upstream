## Description: <br>
AI Agent Skill for GitHub project analysis and nad.fun token launch. Analyzes repos, generates token identity/promo, and launches on nad.fun. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[starrftw](https://clawhub.ai/user/starrftw) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Tokenbroker to analyze GitHub projects, generate token identity and promotional materials, and prepare nad.fun launch assets for user-approved token launches on Monad. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crypto token launch workflows can create financial, legal, or reputation exposure. <br>
Mitigation: Use testnet first, require explicit user approval for launch details, confirm every external upload and on-chain action, and review generated promotional copy for compliance, accuracy, and risk disclosure. <br>
Risk: The workflow may involve private keys, GitHub tokens, API keys, and repository data. <br>
Mitigation: Use host-injected credentials with least privilege, avoid high-value private keys, keep .env local and gitignored, and rotate tokens regularly. <br>
Risk: External calls may send token images, metadata, repository-derived data, and launch details to GitHub, nad.fun, Monad RPC, or dependency skills. <br>
Mitigation: Review destinations, payloads, and selected network before running; avoid scanning or uploading sensitive projects without permission. <br>


## Reference(s): <br>
- [Tokenbroker ClawHub Skill Page](https://clawhub.ai/starrftw/skills/tokenbroker) <br>
- [Tokenbroker Skill Definition](SKILL.md) <br>
- [Token Asset Generation](METADATA.md) <br>
- [Token Launch Orchestration](LAUNCH.md) <br>
- [Repository Tracking](GITHUB.md) <br>
- [Installation and Configuration](SETUP.md) <br>
- [nad.fun Skill Documentation](https://nad.fun/skill.md) <br>
- [monad-development Skill Reference](https://gist.github.com/moltilad/31707d0fc206b960f4cbb13ea11954c2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with TypeScript examples, JSON-like launch metadata, generated promotional copy, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May perform external GitHub, nad.fun API, Monad RPC, and delegated on-chain workflows when configured and approved.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata); artifact frontmatter reports 1.01 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
