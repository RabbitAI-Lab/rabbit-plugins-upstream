## Description:

Security toolkit for AI workflows. Use when scanning code or repos for vulnerabilities, auditing third-party skills/MCPs/agent configs before installing, evaluating shell commands before running them, or generating secure design questions for new features. Provides `rafter run` (remote SAST + SCA, needs RAFTER_API_KEY), `rafter secrets` (offline secrets-only), `rafter agent exec --dry-run` (command-risk classification), and `rafter skill review`.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafter](https://clawhub.ai/user/rafter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to scan repositories for vulnerabilities and exposed secrets, assess shell commands, and review third-party skills and agent configurations before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The `rafter run` workflow performs remote code analysis, so private code may be sent to a cloud service.

Mitigation: Review the service's data handling before scanning private code, and enable only the integrations you intend to use. Use `rafter secrets` when an offline secrets-only scan is sufficient.

Risk: The supplied skill documentation does not include the external `rafter` executable or cloud service, so their behavior and security guarantees were not reviewed in this release evidence.

Mitigation: Review the CLI and service documentation and treat scan results as guidance to inspect before acting.

## Reference(s):

- [Rafter](https://rafter.so)
- [Rafter Security on ClawHub](https://clawhub.ai/rafter/skills/rafter-security)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance and reports, shell command examples, and structured JSON scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command and configuration examples are provided for the user's environment; scan output may include redacted findings.]

## Skill Version(s):

0.11.7 (source: skill frontmatter; server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
