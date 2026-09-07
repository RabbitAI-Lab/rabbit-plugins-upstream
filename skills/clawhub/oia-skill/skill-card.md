## Description:

Initializes Deno + Fresh web projects with the oia framework using @oia-ai/oia-fresh, including environment checks, scaffold generation, development server startup, and local verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pankitgg](https://clawhub.ai/user/pankitgg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill in Claude Code to create an oia framework web app, then run and verify the generated Deno + Fresh project locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running npx commands for @oia-ai packages can fetch and execute code from npm.

Mitigation: Install only if you trust the @oia-ai packages, and prefer a scoped project install unless global availability is required.

Risk: The Deno curl-to-shell installer path can execute a downloaded script.

Mitigation: Use a trusted package manager where possible, or inspect the official installer before running it.

Risk: Initializing into an existing non-empty directory can write or overwrite scaffold template files.

Mitigation: Confirm the target directory choice before initialization and keep existing work under version control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pankitgg/skills/oia-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local project scaffolding, development server startup, and HTTP verification.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
