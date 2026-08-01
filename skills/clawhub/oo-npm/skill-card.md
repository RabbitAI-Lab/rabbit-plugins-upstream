## Description: <br>
Use npm through the OOMOL connector for package search, package metadata, download metrics, version details, current-user lookup, and security advisory queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect npm registry data through an OOMOL-connected account, including package search, manifests, download counts, and security advisories. It is suited for read-oriented npm research and package due diligence workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on OOMOL as an intermediary for npm lookups and connected-account access. <br>
Mitigation: Install only when that trust relationship is acceptable, and review the live action schema before use. <br>
Risk: Future connector actions could introduce write or destructive npm behavior. <br>
Mitigation: Require explicit user approval before running any write or destructive npm action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-npm) <br>
- [npm homepage](https://www.npmjs.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; responses may include JSON data and an execution ID.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
