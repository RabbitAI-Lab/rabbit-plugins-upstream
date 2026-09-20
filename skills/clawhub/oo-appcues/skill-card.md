## Description:

Appcues helps agents read, list, publish, and unpublish Appcues Flow 2.0 experiences and content tags through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Appcues content through the oo CLI, including reading flows and tags and performing controlled publish or unpublish actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute unreviewed installation code if run automatically.

Mitigation: Verify the oo CLI installer through OOMOL's official documentation or a safer package-manager/checksum flow, and require explicit approval before running setup commands.

Risk: Publish and unpublish actions can change or remove Appcues content.

Mitigation: Fetch the live action schema first, review the exact payload and expected effect, and require user confirmation before write actions or explicit approval before destructive actions.

## Reference(s):

- [Appcues homepage](https://www.appcues.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Appcues skill](https://clawhub.ai/oomol/skills/oo-appcues)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses schema-first command construction and returns connector responses as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
