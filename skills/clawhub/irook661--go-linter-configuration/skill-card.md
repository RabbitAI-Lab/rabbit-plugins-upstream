## Description: <br>
Configure and troubleshoot golangci-lint for Go projects. Handle import resolution issues, type-checking problems, and optimize configurations for both local and CI environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[irook661](https://clawhub.ai/user/irook661) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to configure golangci-lint for Go projects, troubleshoot import and type-checking failures, and choose local or CI-friendly lint settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installer commands can run unverified remote code or write to system tool locations. <br>
Mitigation: Review installation steps before use and prefer trusted package managers, pinned releases, or checksummed artifacts for Go and golangci-lint. <br>
Risk: Lint guidance may recommend configurations that hide type-checking or dependency-resolution problems in CI. <br>
Mitigation: Use the minimal configuration only when needed for constrained CI environments and review standard lint coverage before adopting it as the default. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/irook661/skills/go-linter-configuration) <br>
- [Publisher profile](https://clawhub.ai/user/irook661) <br>
- [Go 1.21.5 Linux AMD64 archive](https://golang.org/dl/go1.21.5.linux-amd64.tar.gz) <br>
- [golangci-lint install script](https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with YAML and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes minimal and standard .golangci.yml examples, troubleshooting steps, and CI workflow guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
