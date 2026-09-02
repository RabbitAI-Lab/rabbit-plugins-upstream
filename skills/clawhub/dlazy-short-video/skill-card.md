## Description:

Generates finished 15-25 second vertical social videos for TikTok, YouTube Shorts, Reels, Douyin, and similar platforms using a hook-first storyboard, per-shot visuals, TTS voiceover, Remotion assembly, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to start or continue dLazy short-video projects from the CLI and produce vertical social-media video deliverables rather than scripts. It is suited to general social shorts; the artifact directs conversion-focused product ads to a different skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests and prompts are sent to the dLazy hosted API.

Mitigation: Use the skill only for content approved for dLazy's hosted service.

Risk: Files attached with --files are uploaded to dLazy storage.

Mitigation: Attach only files that are intended to be uploaded and shared with the service.

Risk: The CLI requires a dLazy API key stored locally or supplied through the environment.

Mitigation: Use the documented login or auth flow, protect local credentials, and rotate or revoke the key from the dLazy dashboard when access should be removed.

Risk: A global npm install persists the dLazy CLI on the local system.

Mitigation: Use the pinned npx command for non-persistent execution or review the pinned package before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with bash command examples; generated projects can return a vertical MP4 file through the dLazy service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Attached local files are uploaded to dLazy storage before being referenced by the hosted service.]

## Skill Version(s):

1.2.12 (source: evidence release metadata; artifact frontmatter reports 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
