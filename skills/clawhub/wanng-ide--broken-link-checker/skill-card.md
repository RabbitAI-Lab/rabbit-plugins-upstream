## Description:

Verifies external HTTP and HTTPS URLs for availability using 200-399 status codes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wanng-ide](https://clawhub.ai/user/wanng-ide)

### License/Terms of Use:


## Use Case:

Developers and documentation maintainers use this skill to check whether external links in documentation or reference material are reachable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accepts arbitrary HTTP URLs and could be used to probe local or internal network services from machines with private network access.

Mitigation: Review before installing on machines with access to private services, development servers, VPNs, or cloud metadata endpoints; block loopback, private, link-local, reserved, and localhost destinations before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wanng-ide/skills/broken-link-checker)

## Skill Output:

**Output Type(s):** [JSON, Shell commands]

**Output Format:** [JSON array of URL result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each result includes the URL, validity, and either an HTTP status code or an error value.]

## Skill Version(s):

1.0.0 (source: package.json and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
