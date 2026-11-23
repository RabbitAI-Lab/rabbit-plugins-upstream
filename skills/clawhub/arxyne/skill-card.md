## Description:

Run an engineering simulation and read its result with Arxyne, and register a solver image the user built. Use when the user asks to run a CFD, structural, crash, thermal, acoustic or electromagnetic case, asks which solvers or products are available, wants the numbers and provenance of a past run, or wants to run their own solver image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arxyne](https://clawhub.ai/user/arxyne)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers can use an agent to discover available solvers, run CFD and other engineering simulations, inspect recorded results, save product values, and register compatible solver images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup command downloads a remote installer and runs it without a version or authenticity check.

Mitigation: Review the installer source, verify its release, consider a version-pinned installation, and avoid running an unverified script on a system with sensitive files or credentials.

## Reference(s):

- [Build a custom solver for Arxyne](https://docs.arxyne.com/guide/copy-for-llm/)
- [Community solvers guide](https://docs.arxyne.com/guide/community-solvers/)

## Skill Output:

**Output Type(s):** [Text, Analysis, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with reported simulation results and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports recorded values and run provenance as provided by Arxyne.]

## Skill Version(s):

1.0.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
