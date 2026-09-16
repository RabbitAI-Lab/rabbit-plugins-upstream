## Description:

SiteSpeakAI helps agents operate SiteSpeakAI through the OOMOL oo CLI to read, query, create, update, and delete chatbot-related data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and support teams use this skill to inspect SiteSpeakAI chatbot settings, users, conversations, leads, sources, suggested messages, and updated answers. They can also query chatbots and manage updated-answer entries with confirmation for write and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends installer commands that execute downloaded code directly.

Mitigation: Review setup commands before installation and prefer verified, versioned, signed, or checksum-validated oo CLI sources.

Risk: Write and destructive actions can change or delete SiteSpeakAI data.

Mitigation: Confirm the exact action target, payload, and expected effect with the user before running write or delete actions.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-sitespeakai)
- [SiteSpeakAI Homepage](https://sitespeak.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before running actions; responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
