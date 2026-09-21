## Description:

IPinfo enables agents to run IPinfo lookups and related enrichment actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to look up current or specified IP addresses, enrich IP data, inspect token and account usage metadata, and create IPinfo map reports when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger sensitive current-IP and third-party IP lookups.

Mitigation: Use it only for explicit IPinfo lookup tasks and confirm the target IPs or current-IP behavior before running actions that expose location, organization, privacy, or related enrichment data.

Risk: The map action can upload large IP lists and returns a generated report URL.

Mitigation: Confirm bulk payloads and the intended report generation with the user before invoking the write action.

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified oo CLI installation method and review installer commands before running them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ipinfo-io)
- [IPinfo homepage](https://ipinfo.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include IP geolocation, enrichment data, account metadata, and report URLs depending on the action and IPinfo account scope.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
