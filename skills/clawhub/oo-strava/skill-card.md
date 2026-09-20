## Description:

Strava lets an agent read, create, and update Strava data through an OOMOL-connected account using the oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Strava through an OOMOL-connected account, including reading athlete, activity, route, club, gear, zone, segment, effort, stream, comment, kudoer, and lap data. With user confirmation for write actions, it can create and update activities, upload GPX, TCX, or FIT files, export routes, and favorite or unfavorite segments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute arbitrary local code if the installer source is compromised or not reviewed.

Mitigation: Review the oo CLI installation method before installing; prefer an official, version-pinned installer or manually inspect and verify the downloaded script before execution.

Risk: Write actions can change Strava account state, including creating or updating activities, uploading activity files, and starring or unstarring segments.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write or destructive.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-strava)
- [Strava](https://www.strava.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, connector action names, JSON request payloads, and guidance to confirm Strava write actions before execution.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
