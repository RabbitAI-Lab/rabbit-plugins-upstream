## Description:

MeetGeek helps agents retrieve MeetGeek meeting details, summaries, transcripts, highlights, insights, teams, and meeting lists through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read MeetGeek meeting records, including summaries, transcripts, highlights, insights, team meetings, and available teams. It is intended for accounts that already have MeetGeek connected through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes running a remote installer directly in a shell.

Mitigation: Review the installer source before use and prefer a verified, version-pinned installation method when available.

Risk: Meeting summaries, transcripts, highlights, and insights may contain sensitive meeting data.

Mitigation: Use only with an authorized connected MeetGeek account and limit requests to meetings the user is permitted to access.

## Reference(s):

- [MeetGeek homepage](https://meetgeek.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-meet-geek)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides read-oriented MeetGeek connector actions; connector responses are JSON when commands are executed.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
