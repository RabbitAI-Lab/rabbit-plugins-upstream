## Description: <br>
Provides agent guidance for reading Teamtailor departments, jobs, locations, and job details through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and recruiting teams use this skill to let an agent inspect Teamtailor connector schemas and read departments, jobs, locations, and individual job records through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Teamtailor job, department, and location data through an OOMOL-connected account. <br>
Mitigation: Install and use it only where that Teamtailor read access is intended, and keep OOMOL and Teamtailor account permissions aligned with the agent's task. <br>
Risk: Authentication or connection setup could grant account access if approved unexpectedly. <br>
Mitigation: Approve OOMOL sign-in or Teamtailor connection steps only when intentionally connecting the account for this skill. <br>
Risk: Future versions could add write or destructive actions. <br>
Mitigation: Review security evidence, action tags, and live schemas before upgrading, and require explicit user confirmation for any write or destructive action. <br>


## Reference(s): <br>
- [ClawHub Teamtailor skill page](https://clawhub.ai/oomol/skills/oo-teamtailor) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Teamtailor homepage](https://www.teamtailor.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides read-only Teamtailor actions; connector command responses are JSON when run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
