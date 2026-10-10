## Description:

Guides developers in building Go services with the clone-and-own servicepack template, including concurrent workers, startup dependencies, retries, and graceful shutdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to scaffold and maintain Go applications with multiple long-running services, from local development through deployment as one binary or separate services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented make own step rewrites project files and resets Git history in the clone.

Mitigation: Run it only in a fresh clone after confirming the target module path.

Risk: Build and update commands can change project files or run tools against sensitive code.

Mitigation: Review Make targets before running them; keep custom service code outside framework-owned files that updates overwrite.

## Reference(s):

- [servicepack setup guide](references/setup.md)
- [servicepack project homepage](https://github.com/psyb0t/servicepack)
- [servicepack ClawHub release](https://clawhub.ai/psyb0t/skills/servicepack)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers project setup, service implementations, and build commands.]

## Skill Version(s):

1.9.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
