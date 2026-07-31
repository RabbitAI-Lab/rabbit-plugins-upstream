## Description: <br>
Use this skill for Pinboard (pinboard.in) requests: reading, creating, updating, and deleting data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate their Pinboard account through OOMOL, including reading bookmarks, adding or replacing bookmarks, deleting bookmarks, listing recent bookmarks, listing tags, and checking the latest update time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bookmark additions and replacements can change Pinboard state. <br>
Mitigation: Review the exact action payload and expected effect with the user before approving write operations. <br>
Risk: Deleting a bookmark removes user data from Pinboard. <br>
Mitigation: Confirm the target URL and obtain explicit user approval before running destructive delete operations. <br>
Risk: The skill depends on an installed, signed-in OOMOL CLI with a connected Pinboard account. <br>
Mitigation: Use first-time setup steps only after an auth, connection, or missing-command failure, and avoid proactively opening auth flows. <br>


## Reference(s): <br>
- [ClawHub Pinboard skill page](https://clawhub.ai/oomol/skills/oo-pinboard) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Pinboard homepage](https://pinboard.in/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read actions can run directly; bookmark additions, replacements, and deletions require careful review before approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact/SKILL.md frontmatter and evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
