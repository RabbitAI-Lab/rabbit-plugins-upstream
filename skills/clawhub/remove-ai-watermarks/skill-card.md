## Description:

Guides an agent to inspect and remove AI watermarks and provenance marks from user-owned or user-authorized images and video using the remove-ai-watermarks CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to drive a local or hosted CLI workflow for identifying and removing AI provenance marks from media they own or are authorized to modify. The skill also guides the agent to refuse third-party paid-asset watermark removal and deceptive origin claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill could be misused to remove marks from third-party paid or copyrighted assets.

Mitigation: Use only for media the user owns or is authorized to modify, and refuse stock-agency, marketplace, classifieds, tiled-preview, or similar third-party asset marks.

Risk: Removing a local watermark or metadata field could be misrepresented as proof that media is human-made.

Mitigation: Report removal results narrowly and do not claim that edited media is clean, human-made, or free of server-side generation history.

Risk: Pixel, invisible, or video operations may fail or produce partial results when dependencies such as CUDA, ffmpeg, or CLI extras are missing.

Mitigation: Run the bundled probe before choosing commands, follow its advice, and use isolated uv or pipx installs when additional extras are needed.

Risk: A guessed region or guessed vendor route could remove content without a reliable signal.

Mitigation: Identify first unless the user already named a removal, require user-supplied regions for erase operations, and set vendor-specific invisible removal only when the user confirms the source.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Project Homepage](https://raiw.cc)
- [Source Repository](https://github.com/wiltodelta/remove-ai-watermarks)
- [Command Recipes](references/commands.md)
- [Install Extras](references/install.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and command-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only commands actually run, their exit codes, and confirmed output paths; does not claim a file is clean or human-made.]

## Skill Version(s):

1.0.6 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
