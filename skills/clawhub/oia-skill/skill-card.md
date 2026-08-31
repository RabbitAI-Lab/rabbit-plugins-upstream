## Description:

Initializes Deno + Fresh web projects with the oia framework by checking the environment, running the @oia-ai/oia-fresh scaffold command, starting the development server, and verifying the generated page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pankitgg](https://clawhub.ai/user/pankitgg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create a new oia-fresh application, validate that Deno and npx are available, start the local dev server, and report setup status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create a new project directory and run npm or Deno tooling from the network.

Mitigation: Review network-fetched installers and scaffold commands before execution, and run the skill in a workspace where file creation is expected.

Risk: The skill may optionally install Deno and briefly start a local development server.

Mitigation: Confirm Deno installation steps with the user when needed and stop the temporary development server after the page verification completes.

Risk: Global installation makes the skill available outside the current project.

Mitigation: Prefer local installation unless the user intentionally wants the skill available across projects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pankitgg/skills/oia-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create project files, install or invoke Deno/npm tooling, start a temporary local development server, and summarize verification results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
