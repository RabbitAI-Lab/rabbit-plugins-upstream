## Description:

Helcim connector skill for reading, creating, and updating customer data through OOMOL's oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Helcim customer workflows through an OOMOL-connected account, including customer creation, retrieval, search, and updates. The skill is suited for agents that need to inspect live action schemas before issuing Helcim connector calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path directs users to execute a remote installer in a shell.

Mitigation: Use the documented installer only after independently checking the installer source or integrity and confirming trust in OOMOL's delivery path.

Risk: Customer create and update actions can change Helcim account data.

Mitigation: Inspect the live action schema, prepare the exact payload, and obtain user confirmation before running write actions.

## Reference(s):

- [ClawHub Helcim Skill](https://clawhub.ai/oomol/skills/oo-helcim)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Helcim homepage](https://www.helcim.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require user confirmation; connector payloads should be based on the live action schema.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
