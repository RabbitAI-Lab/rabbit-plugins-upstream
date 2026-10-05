## Description:

Discovers AWS-hosted AI agents and related workloads and writes canonical inventory JSON for optional local agent-bom analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AWS AI agents and related workloads in approved accounts and regions. They can optionally scan or export the resulting inventory on request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS discovery exposes the selected account's resource inventory to the agent and local output files.

Mitigation: Use an operator-approved read-only profile with short-lived credentials; review account, regions, services, and output path before running.

Risk: An inventory scan or handoff could share cloud resource details beyond the intended discovery step.

Mitigation: Keep discovery-only as the default and require explicit operator approval for any scan, export, or external handoff.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [Project homepage (listed in skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON inventory files]

**Output Format:** [Markdown guidance and commands; canonical inventory JSON when run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery only by default; scanning and exports require operator approval.]

## Skill Version(s):

0.108.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
