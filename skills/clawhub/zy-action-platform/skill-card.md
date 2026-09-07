## Description:

Connect and operate ZY Action Platform (AI Business Action System): guide local install & DeepSeek key config, then health-check/login and, across the five products AIP/Foundry/Gotham/Apollo/Swift, run natural-language data queries, list/run automation workflows, query datasets/ontology, search intel, inspect deployments and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youkpan](https://clawhub.ai/user/youkpan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to ZY Action Platform, guide local setup, authenticate to platform services, and run data queries, workflow automation, dataset and ontology lookups, intel search, and deployment inspections across the platform's product services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broad authenticated API requests to configured ZY Action Platform services, including a generic request command.

Mitigation: Use trusted platform endpoints, confirm write, delete, publish, or bulk operations before execution, and scope commands to the product and path the user requested.

Risk: Credentials and platform tokens may be handled during login and cached locally.

Mitigation: Do not display passwords or tokens in chat, prefer --no-cache where practical, rotate the default admin password immediately, and reauthenticate only through the intended platform endpoint.

Risk: Remote plaintext HTTP base URLs can expose credentials or data in transit.

Mitigation: Prefer local loopback or trusted HTTPS endpoints for remote access and avoid sending credentials to untrusted base URLs.

Risk: The Windows platform package is downloaded outside this skill artifact.

Mitigation: Verify the package source and publisher before running it, and install only when the ZY publisher and endpoint are trusted.

## Reference(s):

- [ZY Action Platform API Quick Reference](references/api-spec.md)
- [ZY Action Platform Session Examples](references/examples.md)
- [ZY Action Platform Product Page](https://zyinfo.pro/action/)
- [ClawHub Skill Page](https://clawhub.ai/youkpan/skills/zy-action-platform)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include REST client command output summaries, setup steps, API request guidance, and platform operation recommendations.]

## Skill Version(s):

1.0.1 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
