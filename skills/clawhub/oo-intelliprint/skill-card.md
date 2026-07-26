## Description: <br>
Use this skill to search and read Intelliprint data from intelliprint.net. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent read Intelliprint backgrounds, mailing lists, recipients, and print jobs through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mailing lists, recipients, and print jobs may contain business or customer information. <br>
Mitigation: Use the skill for read-only lookup tasks through an authorized OOMOL-connected account and avoid exposing retrieved data beyond the user's requested task. <br>
Risk: Future connector actions could write, overwrite, or delete Intelliprint data if added later. <br>
Mitigation: Require explicit user confirmation before running any action tagged write or destructive. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-intelliprint) <br>
- [Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Intelliprint Homepage](https://www.intelliprint.net) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only Intelliprint lookup guidance and oo CLI commands; connector responses are JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
