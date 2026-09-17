## Description:

Tomba (tomba.io). Use this skill for ANY Tomba request - searching and reading data. Whenever a task involves Tomba, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Tomba through an OOMOL-connected account for domain searches, professional email discovery, email verification, enrichment, company search, technology detection, and account lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented fallback setup includes mutable remote installer pipe commands for the oo CLI.

Mitigation: Install the oo CLI through a verified, inspectable, versioned method instead of running installer pipe commands automatically.

Risk: The skill can query Tomba account-connected data and external contact intelligence.

Mitigation: Use only with a Tomba/OOMOL account the user intends to query and fetch each action's live schema before sending payloads.

## Reference(s):

- [Tomba homepage](https://tomba.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tomba)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; responses may include JSON data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
