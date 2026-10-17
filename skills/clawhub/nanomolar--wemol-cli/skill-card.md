## Description:

Use when a task may involve Wemol, a drug-discovery computing platform that integrates many biology, AI, and chemistry modules for workflows such as biologics design, small-molecule discovery, molecular simulation, ADMET prediction, virtual screening, structure prediction, antibody engineering, and immunogenicity analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nanomolar](https://clawhub.ai/user/nanomolar)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Wemol CLI for biology, chemistry, and AI workflows: discovering modules or flows, checking live schemas, submitting jobs, monitoring progress, troubleshooting failures, and retrieving outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands retrieve mutable remote scripts and the referenced macOS and Windows builds may trigger platform security warnings.

Mitigation: Prefer a pinned version and a download-verify-run process, and do not bypass Gatekeeper or SmartScreen unless the exact Wemol binary and source have been independently verified.

Risk: Non-interactive login can place usernames and passwords in command history, logs, or process listings.

Mitigation: Prefer interactive login and cached sessions; when automation is unavoidable, use a secure secret channel and avoid exposing passwords directly on the command line.

## Reference(s):

- [Install](references/install.md)
- [Session And Host](references/session-and-host.md)
- [Module Workflow](references/module-workflow.md)
- [Flow Workflow](references/flow-workflow.md)
- [Job Workflow](references/job-workflow.md)
- [Output And Agent Notes](references/output-and-agent-notes.md)
- [Wemol Service Host](https://wemol.wecomput.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI command sequences, parameter-schema guidance, status interpretation, and artifact download or recovery steps.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
