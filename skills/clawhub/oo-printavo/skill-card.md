## Description: <br>
Printavo helps agents search and read Printavo account data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill on behalf of Printavo users to retrieve account information and list contacts, customers, orders, and tasks from an OOMOL-connected Printavo account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Printavo business data through the user's OOMOL-connected account. <br>
Mitigation: Install it only for users who accept that access, and review OOMOL's CLI and Printavo connection setup before first use. <br>
Risk: First-time setup recovery can install or authenticate the oo CLI. <br>
Mitigation: Run setup commands only after a missing-CLI, authentication, connection, or billing failure; do not initiate login or connection proactively. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-printavo) <br>
- [Printavo Homepage](https://www.printavo.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches the live connector schema before action payload construction; documented actions are read-only.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
