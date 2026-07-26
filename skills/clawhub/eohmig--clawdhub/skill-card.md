## Description: <br>
Use the ClawdHub CLI to search, install, update, and publish agent skills from clawdhub.com. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eohmig](https://clawhub.ai/user/eohmig) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to get concise ClawdHub CLI command guidance for searching, installing, updating, listing, authenticating, and publishing agent skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk or forced update commands can change many installed skills without individual review. <br>
Mitigation: Avoid --all, --force, and --no-input unless broad updates are intended; inspect affected skill folders before reuse or publication. <br>
Risk: Publishing commands can upload local skill contents and release notes to a registry. <br>
Mitigation: Review the target skill folder, version, slug, and changelog before running publish commands. <br>


## Reference(s): <br>
- [Clawdhub Skill Page](https://clawhub.ai/eohmig/skills/clawdhub) <br>
- [ClawdHub Registry](https://clawdhub.com) <br>
- [clawdhub npm Package](https://www.npmjs.com/package/clawdhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash command blocks and concise CLI notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands assume the clawdhub CLI binary is installed and available on PATH.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
