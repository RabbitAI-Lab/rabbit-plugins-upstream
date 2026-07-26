## Description: <br>
Kontent.ai helps agents search and read Kontent.ai content through an OOMOL-connected account instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect Kontent.ai action schemas and read content items, content types, and languages through an OOMOL-connected Kontent.ai account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The manifest routes broadly for Kontent.ai tasks even though the currently listed actions are read-only. <br>
Mitigation: Use the live action schema before building each payload, and treat any future write or destructive action tags as requiring explicit user confirmation. <br>
Risk: The skill depends on oo CLI installation, OOMOL authentication, a connected Kontent.ai account, valid scopes, active credentials, and OOMOL billing status. <br>
Mitigation: Follow setup or recovery steps only after the corresponding command error appears, and avoid asking users to provide raw Kontent.ai tokens in prompts or scripts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kontent-ai) <br>
- [Kontent.ai Homepage](https://kontent.ai) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata through the oo CLI.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
