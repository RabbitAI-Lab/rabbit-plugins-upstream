## Description: <br>
Adyen helps agents search and read Adyen company, merchant, and API credential details through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect Adyen account data through the OOMOL oo CLI, including company accounts, merchant accounts, and the connected API credential. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates through OOMOL as an intermediary for an Adyen account. <br>
Mitigation: Install and use it only after reviewing the OOMOL connection scopes and confirming that this intermediary access is acceptable. <br>
Risk: Setup commands can install the oo CLI or start an authentication flow if run unnecessarily. <br>
Mitigation: Run setup steps only after an auth, connection, or missing-CLI failure, as the artifact directs. <br>
Risk: Future connector actions could change or delete Adyen data if write or destructive actions are added. <br>
Mitigation: Require explicit user confirmation of the exact payload and effect before any write or destructive Adyen action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-adyen) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Adyen homepage](https://www.adyen.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to fetch the live connector schema before running an Adyen action.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
