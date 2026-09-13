## Description:

Removes and identifies AI watermarks and provenance marks in images and video the user generated or edited, while excluding third-party paid-asset watermarks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through identifying and removing supported AI provenance signals from media they own or are allowed to alter. It also helps route unsupported or unsafe requests away from removal, including third-party paid-asset watermarks and deceptive provenance claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to inspect local CLI, GPU, ffmpeg, and installer availability.

Mitigation: Review the probe behavior before use and run it only in an environment where local capability inspection is acceptable.

Risk: The skill can direct installation or upgrade of an external CLI without pinning a package version.

Mitigation: Require explicit approval for installation or upgrade steps and pin a reviewed package version where operational policy requires reproducible tooling.

Risk: Watermark removal can be misused on third-party commercial assets or to support deceptive origin claims.

Mitigation: Use the skill only on media the user owns or is allowed to alter, refuse third-party paid-asset watermark removal, and do not present edited generated content as human-made.

## Reference(s):

- [Remove AI Watermarks ClawHub page](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [remove-ai-watermarks repository](https://github.com/wiltodelta/remove-ai-watermarks)
- [raiw.cc](https://raiw.cc)
- [Command recipes](references/commands.md)
- [Install extras](references/install.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Markdown with inline shell commands and concise status reporting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create or modify media output files only when the workflow selects a removal route and an output path is provided.]

## Skill Version(s):

1.0.8 (source: server release metadata and SKILL.md frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
