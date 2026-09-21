## Description:

Servicepack helps agents guide developers through creating Go services from the psyb0t/servicepack template, including service scaffolding, dependency ordering, readiness gating, retries, lifecycle hooks, logging, configuration, build, test, and Docker-backed workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build or modify Go servicepack projects that run related services together locally and can later be deployed as one binary or split into separate microservices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup workflow can rewrite module files and reset git history when running the ownership command in a cloned template repository.

Mitigation: Run ownership setup only in a fresh clone or intended project workspace, and review the setup notes before executing commands.

Risk: Docker-backed build and development targets may pull or build local development images.

Mitigation: Use an environment where Docker image builds are expected and allowed, and review generated commands before running them.

Risk: Framework-owned files can be overwritten by servicepack update workflows.

Mitigation: Keep custom behavior in documented extension points such as service files, lifecycle hooks, and custom command files.

## Reference(s):

- [Setup reference](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/servicepack)
- [Project homepage](https://github.com/psyb0t/servicepack)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline Go code and bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated service scaffolding guidance, Make target commands, configuration notes, and file-editing recommendations.]

## Skill Version(s):

1.9.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
