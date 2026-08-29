## Description:

fn-fpk guides agents through developing, packaging, testing, and publishing fnOS FPK applications, including Native and Docker app structures, manifests, privileges, lifecycle scripts, Open API access, and fnpack/appcenter-cli workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dalingo81](https://clawhub.ai/user/dalingo81)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or update fnOS FPK apps, configure permissions, resources, UI entries, lifecycle scripts, and wizards, package with fnpack, test with appcenter-cli, and integrate fnOS Open API capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples involving root mode can lead to excessive application privileges.

Mitigation: Use the default package user mode unless root privileges are explicitly required and approved.

Risk: Broad file authorization scopes can expose more user data than an app needs.

Mitigation: Declare only the fnOS Open API scopes the app actually uses and validate user permissions before reading, writing, or deleting files.

Risk: appcenter-cli installation examples can modify a live fnOS device during testing.

Mitigation: Run install and install-local commands only against intended development or test devices and review package contents before installation.

Risk: Uninstall examples may delete user data when configured to do so.

Mitigation: Make deletion choices explicit in uninstall flows and preserve app data unless the user intentionally selects deletion.

## Reference(s):

- [fnOS Developer Documentation](https://developer.fnnas.com)
- [fnOS Open API Overview](https://developer.fnnas.com/api/overview/)
- [fnpack 1.2.3 Downloads](https://static2.fnnas.com/fnpack/fnpack-1.2.3-{os}-{arch})

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, code blocks, and JSON/INI configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
