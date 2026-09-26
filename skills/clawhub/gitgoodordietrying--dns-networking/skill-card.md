## Description:

Debug DNS resolution and network connectivity. Use when troubleshooting DNS failures, testing port connectivity, diagnosing firewall rules, inspecting HTTP requests with curl verbose mode, configuring /etc/hosts, or debugging proxy and certificate issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to diagnose DNS resolution, port connectivity, firewall behavior, HTTP request failures, proxy configuration, and TLS certificate issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privileged firewall commands using sudo with iptables, ufw, or socketfilterfw can persist or disrupt network access.

Mitigation: Treat those commands as administrative changes, review current rules first, run them only with explicit intent, and plan a rollback before applying changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gitgoodordietrying/skills/dns-networking)
- [ClawHub publisher profile](https://clawhub.ai/user/gitgoodordietrying)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires applicable networking tools such as dig, nslookup, curl, ping, or nc.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
