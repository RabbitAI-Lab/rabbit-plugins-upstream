## Description:

Splunk HTTP Event Collector (splunk.com). Use this skill for Splunk HTTP Event Collector requests to inspect action schemas and send structured or raw events through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect the live Splunk HTTP Event Collector action schema and send structured or raw HEC events through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes remote installer commands for the oo CLI, including curl-to-bash and irm-to-iex patterns.

Mitigation: Use a verified, pinned, user-reviewed installation method before allowing an agent to run setup commands.

Risk: Splunk HEC payloads may include confidential, personal, credential-related, or regulated log data.

Mitigation: Confirm every event payload with the user before write actions and avoid sending sensitive data unless the user has approved it.

Risk: The security verdict is suspicious because payloads are sent through OOMOL and the routing instructions are broad.

Mitigation: Install only if the user accepts OOMOL-mediated Splunk HEC operations and review the generated action schema before each request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-splunk-http-event-collector)
- [Splunk HTTP Event Collector homepage](https://www.splunk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to fetch action schemas and submit JSON payloads to the connected Splunk HEC service.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
