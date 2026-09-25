## Description:

Resolve hostnames to IP addresses using `dig` from bind-utils.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xejrax](https://clawhub.ai/user/xejrax)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to run common DNS lookups, including A, AAAA, full-record, and reverse lookup queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require installing bind-utils through the system package manager.

Mitigation: Install only in environments where adding bind-utils is approved, and review the package-manager command before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xejrax/skills/dns-lookup)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the dig binary from bind-utils; no credentials or background access requested.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
