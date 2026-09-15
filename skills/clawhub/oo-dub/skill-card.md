## Description:

Dub (dub.co). Use this skill for ANY Dub request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to operate an authenticated Dub workspace through OOMOL-connected credentials. It supports reading links, folders, tags, and analytics, and creating, updating, or deleting Dub resources after the required user confirmations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include a remote installer pattern that downloads and executes code.

Mitigation: Install the oo CLI only through a trusted method, preferably after reviewing or verifying the installer.

Risk: Write and destructive Dub actions can create, update, or delete workspace resources.

Mitigation: Confirm the exact payload, effect, and target with the user before running write or destructive actions.

Risk: Action payloads are sent through OOMOL-connected credentials.

Mitigation: Keep unrelated secrets out of Dub action payloads and inspect the live action schema before sending data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dub)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Dub homepage](https://dub.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI and return JSON responses from the Dub connector.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
