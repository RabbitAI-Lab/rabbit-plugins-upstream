## Description: <br>
Postalytics helps agents search and read campaign, contact, list, and template data from a connected Postalytics account through OOMOL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent retrieve Postalytics campaign details, campaign statistics, contacts, contact lists, and direct-mail template information from an authenticated Postalytics account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read data from the user's connected Postalytics account through OOMOL. <br>
Mitigation: Install and use the skill only when account-level Postalytics read access is intended, and review the oo CLI and OOMOL account connection setup before use. <br>
Risk: Future connector actions could include write or destructive operations even though this release documents read-only behavior. <br>
Mitigation: Do not approve any write or destructive action unless the exact Postalytics target and payload are clear and explicitly confirmed. <br>
Risk: Incorrect action payloads could produce failed or misleading connector requests. <br>
Mitigation: Fetch the live connector schema with `oo connector schema` before constructing each `oo connector run` payload. <br>


## Reference(s): <br>
- [Postalytics homepage](https://www.postalytics.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-postalytics) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON connector payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
