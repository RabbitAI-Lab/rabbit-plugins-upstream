## Description:

Configure and troubleshoot golangci-lint for Go projects, including import resolution issues, type-checking problems, and local or CI configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[irook661](https://clawhub.ai/user/irook661)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to configure golangci-lint, choose practical linter sets, troubleshoot import and type-checking failures, and prepare linting workflows for local development or CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install steps may run unverified internet code or write to system-wide locations.

Mitigation: Review install commands before use, prefer manually installed version-pinned Go and golangci-lint packages, and verify checksums or signatures where available.

Risk: Linter configuration advice may reduce analysis depth when troubleshooting import or type-checking failures.

Mitigation: Use minimal configurations only for constrained CI cases, and review linter coverage before adopting the generated configuration in release workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/irook661/skills/go-linter-configuration)
- [Go download archive](https://golang.org/dl/go1.21.5.linux-amd64.tar.gz)
- [golangci-lint install script](https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, Code]

**Output Format:** [Markdown with inline bash and YAML code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes golangci-lint command examples, .golangci.yml templates, troubleshooting guidance, and a GitHub Actions workflow example.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
