## Description: <br>
Helps agents discover, vet, recommend, and optionally install agent skills for users who need specialized capabilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill when a user asks for help finding installable skills for a task. It guides the agent through search, quality review, recommendation, and optional installation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search results or popular listings can still surface low-quality, untrusted, or mismatched skills. <br>
Mitigation: Review publisher identity, repository reputation, install count, and source code where practical before recommending or installing a skill. <br>
Risk: Global installs with confirmation skipped create persistent changes to the agent environment. <br>
Mitigation: Treat npx skills add with -g -y as a persistent install path; remove -y or ask for explicit confirmation when additional review is desired. <br>


## Reference(s): <br>
- [Find Skills on ClawHub](https://clawhub.ai/seanford/skills/find-skills) <br>
- [Skills Directory](https://skills.sh/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May suggest Skills CLI commands such as npx skills find, npx skills add, npx skills check, and npx skills update.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
