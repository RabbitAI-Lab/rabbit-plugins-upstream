## Description:

Search and read Unsplash photos, topics, and random photo selections through the OOMOL Unsplash connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Unsplash, fetch photo details, list curated topics, and retrieve random or topic-specific public photos through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Do not let an agent automatically run installer pipelines; install the oo CLI through a trusted, verifiable method and manually confirm authentication or account-connection steps.

Risk: The skill depends on an authenticated OOMOL-connected Unsplash account and can fail when authentication, connection scopes, credentials, or billing are unavailable.

Mitigation: Run normal read actions directly only after setup is complete, and handle auth, connection, credential, or billing failures with user-confirmed setup steps.

## Reference(s):

- [Unsplash homepage](https://unsplash.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-unsplash)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented Unsplash actions return JSON data through the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
