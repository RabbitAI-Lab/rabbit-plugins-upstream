## Description:

Operates Spotify through the OOMOL oo CLI so agents can read, search, create, update, and delete Spotify data using live action schemas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect and manage Spotify catalog, library, playlist, and playback data through an OOMOL-connected Spotify account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote installer scripts directly.

Mitigation: Prefer verified official installation steps, inspect downloaded scripts before execution, and avoid administrator privileges.

Risk: Write and destructive Spotify actions can alter playlists, saved content, follows, playback state, queue, volume, shuffle, repeat, or device routing.

Mitigation: Confirm the exact target, payload, and effect before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Spotify skill page](https://clawhub.ai/oomol/skills/oo-spotify)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Spotify homepage](https://spotify.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Spotify connector responses are JSON; the skill expects live schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
