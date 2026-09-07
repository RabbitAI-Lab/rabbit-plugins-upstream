## Description:

VeryEast (最佳东方) job assistant helps job seekers search service-industry jobs, review job details, manage resumes, submit applications, and analyze job fit across VeryEast listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kevinwan12334](https://clawhub.ai/user/kevinwan12334)

### License/Terms of Use:

MIT-0

## Use Case:

External job seekers use this skill to search VeryEast job listings, compare roles, maintain resume information, submit confirmed applications, and receive job-fit guidance for hotel, catering, beauty, wellness, retail, e-commerce, and other service-industry roles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a user's VeryEast account, resume data, and job-application workflow.

Mitigation: Review the skill before installing, authorize only the intended account, and clear the stored credential when finished.

Risk: Resume edits and job applications can change real account data or submit real applications.

Mitigation: Confirm each resume edit and application target with the user before executing account-changing actions.

Risk: Local authorization material could be exposed if the config file or authorization code is shared.

Mitigation: Do not share config.json or authorization codes; prefer the VEAST_API_KEY environment variable where appropriate.

Risk: The client reports the host agent name to the VeryEast endpoint.

Mitigation: Inform reviewers and users who need to account for platform-identifying request metadata.

## Reference(s):

- [Agent execution guide](references/agent-guide.md)
- [VeryEast assistant API reference](references/api.md)
- [Common scenarios](references/scenarios.md)
- [Match scoring dimensions](references/scoring.md)
- [VeryEast homepage](https://www.veryeast.cn)
- [ClawHub skill page](https://clawhub.ai/kevinwan12334/skills/veryeast-assistant)
- [Publisher profile](https://clawhub.ai/user/kevinwan12334)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Human-facing Markdown plus shell command invocations for the bundled Node.js client.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute authenticated VeryEast account actions after local authorization and user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 0.8.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
