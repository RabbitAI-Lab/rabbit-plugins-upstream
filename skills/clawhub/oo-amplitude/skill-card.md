## Description:

Enables agents to search and read Amplitude event and user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Amplitude analytics, inspect live connector schemas, retrieve event segmentation metrics, view user activity, list events, and search users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer one-liners for the oo CLI.

Mitigation: Use a versioned official package or download-and-verify flow before execution, and install only after confirming trust in OOMOL.

Risk: Amplitude queries can expose user activity and event analytics through the connector.

Mitigation: Review query payloads before execution and limit requests to the user's intended scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-amplitude)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Amplitude homepage](https://amplitude.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo connector commands and JSON payloads; connector responses are JSON from Amplitude through OOMOL.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
