## Description: <br>
Use this skill to search and read Emelia campaign, contact, email provider, and webhook data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to inspect Emelia connector schemas and read campaign, activity, contact, email provider, and webhook data from an authenticated OOMOL-connected Emelia account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses OOMOL as an intermediary for read access to Emelia account data. <br>
Mitigation: Install and use it only when that intermediary access model is acceptable for the account and data being queried. <br>
Risk: First-time setup may involve running a remote oo CLI installer command. <br>
Mitigation: Review OOMOL's installer instructions and verify the source before running the remote install command. <br>


## Reference(s): <br>
- [Emelia homepage](https://emelia.io/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-emelia) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return JSON data from read-only Emelia connector actions, including execution metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
