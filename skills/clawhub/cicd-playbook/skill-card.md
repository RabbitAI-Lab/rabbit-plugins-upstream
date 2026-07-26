## Description: <br>
Write a CI/CD pipeline playbook for a service or team. Use when asked to document a CI/CD pipeline, write a deployment process, define release gates, document build and test stages, or create a deployment guide. Produces a structured playbook covering pipeline stages, environment definitions, deployment gates, rollback procedures, and on-call responsibilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to document CI/CD pipelines, deployment gates, rollback procedures, environment setup, and on-call responsibilities for a service or team. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated deployment or rollback commands may be copied into operational workflows before they are adapted and reviewed. <br>
Mitigation: Review generated commands, environment names, deployment targets, and rollback steps with the owning team before operational use. <br>
Risk: A CI/CD playbook can become misleading if placeholders are left unresolved or pipeline gates do not match the live service. <br>
Mitigation: Replace all placeholders with verified service details and validate the final playbook against the actual CI/CD platform, approval process, and on-call model. <br>


## Reference(s): <br>
- [Cicd Playbook on ClawHub](https://clawhub.ai/mohitagw15856/skills/cicd-playbook) <br>
- [Cicd Playbook Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/cicd-playbook.html) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown playbook with tables, checklists, and inline bash command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts for service, stack, CI/CD platform, environments, deployment gates, and on-call details when missing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
