## Description: <br>
Adyntel connector skill for searching ad-library data and reading keyword or ad details through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to query Adyntel for competitive ad intelligence across Google, LinkedIn, Meta, and TikTok, and to retrieve domain keyword metrics or TikTok ad details through their connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Adyntel-related requests can send search terms, company domains, LinkedIn page IDs, or ad IDs to external OOMOL and Adyntel services. <br>
Mitigation: Confirm vague or sensitive queries with the user before running oo connector commands. <br>
Risk: First-time setup includes shell installer commands for the oo CLI. <br>
Mitigation: Review the installer source and run setup only when the oo CLI is missing or authentication or connection errors require it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-adyntel) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Adyntel homepage](https://www.adyntel.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run oo CLI connector commands that return JSON data from Adyntel.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
