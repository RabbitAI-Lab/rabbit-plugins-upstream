## Description:

IP2Proxy helps an agent inspect the live IP2Proxy connector schema and run proxy-detection lookups for IPv4 or IPv6 addresses through the OOMOL `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to check whether an IP address is associated with proxy usage while keeping IP2Proxy credentials mediated through the OOMOL connector. It is suited for agent workflows that need live schema inspection before issuing a read-only IP2Proxy lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path tells users to run installer scripts directly from the web.

Mitigation: Install only from a trusted OOMOL CLI source, prefer a verified or package-managed install path, or inspect installer scripts before running them on sensitive systems.

Risk: IP address lookups and connector execution metadata may be handled by OOMOL and IP2Proxy services.

Mitigation: Use the skill only where sharing lookup targets and related metadata with those services is acceptable under the user's data-handling policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ip2proxy)
- [IP2Proxy Web Service](https://www.ip2location.com/web-service/ip2proxy)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill retrieves the live connector schema before constructing lookup payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
