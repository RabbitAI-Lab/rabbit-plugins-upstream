## Description: <br>
Kaggle helps agents search and read Kaggle competitions, datasets, notebooks, scripts, and models through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill when they want an agent to query Kaggle resources through an existing OOMOL connection instead of calling Kaggle APIs directly. It is focused on read-oriented discovery tasks such as listing competitions, datasets, notebooks, scripts, and models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates through an OOMOL-connected Kaggle account, so connector actions depend on the user's trust in that account connection and CLI toolchain. <br>
Mitigation: Install and use it only when the user wants Kaggle access through OOMOL, and review the live connector schema before running actions. <br>
Risk: Future connector actions could include write, delete, billing, credential, or account-management behavior not present in the current read-oriented artifact evidence. <br>
Mitigation: Require explicit user confirmation before any such action and verify the exact target, payload, and expected effect. <br>
Risk: First-time setup can involve installing the oo CLI, signing in, or connecting Kaggle credentials. <br>
Mitigation: Run setup steps only after an auth, connection, or missing-command failure, and only when the user trusts OOMOL and approves the setup path. <br>


## Reference(s): <br>
- [ClawHub Kaggle skill page](https://clawhub.ai/oomol/skills/oo-kaggle) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Kaggle homepage](https://www.kaggle.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, text, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before running Kaggle actions; current documented actions are read-oriented.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
