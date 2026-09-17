## Description:

SunoAPI routes agent requests for reading, creating, and updating SunoAPI data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to inspect SunoAPI action schemas and run music, lyrics, audio editing, and account-credit operations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A remote installer one-liner could install an unverified oo CLI.

Mitigation: Prefer a verified or package-managed oo CLI installation before using the skill.

Risk: Generation, conversion, upload, extension, separation, and similar actions may create remote or billable SunoAPI tasks without clear user consent.

Mitigation: Confirm the exact payload, files, expected remote effect, and possible credit usage before running those actions.

## Reference(s):

- [SunoAPI homepage](https://sunoapi.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [SunoAPI OOMOL connection](https://console.oomol.com/app-connections?provider=sunoapi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When actions are executed, the connector returns JSON responses with task details or account information.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
