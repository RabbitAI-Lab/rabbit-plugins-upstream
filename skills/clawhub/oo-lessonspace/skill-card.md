## Description:

Lessonspace helps agents manage Lessonspace spaces, organisation sessions, and recording links through an OOMOL-connected CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to create or retrieve Lessonspace spaces, inspect organisation sessions, fetch playback URLs, and list sessions while relying on OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute code from the internet.

Mitigation: Review setup before installing and prefer an official package manager, a version-pinned release, or an installer with a verified checksum or signature.

Risk: Lessonspace write actions can create or retrieve spaces and return join URLs or room credentials.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and limit disclosure of returned access details.

Risk: Read actions may expose session, recording, or room-access information.

Mitigation: Treat returned Lessonspace data as sensitive and share only the fields needed for the user's task.

## Reference(s):

- [Lessonspace homepage](https://www.thelessonspace.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Lessonspace session, recording, join URL, or room credential data returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
