## Description:

Envoy (envoy.com). Use this skill for Envoy requests that read, create, or update data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Envoy connector schemas and run supported Envoy employee, flow, invite, and location actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run oo CLI commands against an authenticated OOMOL account connected to Envoy.

Mitigation: Install only when that level of Envoy access is acceptable, inspect the live action schema before use, and confirm exact payloads before write-labeled actions.

Risk: The skill documents remote installer commands that fetch and execute scripts.

Mitigation: Prefer a verified, pinned installation path for the oo CLI instead of running pasted remote installer commands directly.

## Reference(s):

- [ClawHub Envoy Skill](https://clawhub.ai/oomol/skills/oo-envoy)
- [Envoy homepage](https://envoy.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that call a connected Envoy account and return JSON responses.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
