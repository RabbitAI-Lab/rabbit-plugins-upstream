## Description: <br>
Willhaben CLI for searching Austria's largest classifieds marketplace. Search listings, view details, check seller profiles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pasogott](https://clawhub.ai/user/pasogott) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to install and run whcli for searching willhaben.at listings, viewing listing details, checking seller profiles, and exporting search results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs and invokes CLI code from a Homebrew tap or GitHub repository outside the skill bundle. <br>
Mitigation: Install only when the upstream tap or repository is trusted, and review the external package source first in sensitive environments. <br>
Risk: The artifact notes that the listing detail command has a known bug. <br>
Mitigation: Validate listing detail results before relying on them, and prefer search or seller commands when the detail output is uncertain. <br>
Risk: Location filtering may include nearby regions. <br>
Mitigation: Review returned locations before using search results for location-sensitive decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pasogott/skills/whcli) <br>
- [whcli repository](https://github.com/pasogott/whcli) <br>
- [whcli issues](https://github.com/pasogott/whcli/issues) <br>
- [Homebrew tap](https://github.com/pasogott/homebrew-tap) <br>
- [willhaben.at](https://willhaben.at) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with bash command examples and CLI option tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The documented CLI can produce table, JSON, or CSV output for supported commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
