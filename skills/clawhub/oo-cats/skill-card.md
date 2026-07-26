## Description: <br>
CATS (catsone.com) connector skill for searching and reading CATS data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search and read CATS recruiting data through an OOMOL-connected account, including candidates, companies, jobs, and site information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read candidate and hiring data from a connected CATS account. <br>
Mitigation: Use it only for intended CATS read tasks, limit requests to necessary records, and treat returned recruiting data as sensitive. <br>
Risk: The skill depends on the external oo CLI and an OOMOL account connection. <br>
Mitigation: Review the CLI setup step, use the OOMOL connection flow for credentials, and avoid exposing raw tokens in prompts, files, or command output. <br>


## Reference(s): <br>
- [CATS homepage](https://catsone.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cats) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata when run through the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
