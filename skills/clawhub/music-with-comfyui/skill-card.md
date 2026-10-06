## Description:

Generates original music from a style description and optional lyrics using AceStep Audio 1.5 on a user-configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a music brief or optional lyrics into a generated song, delivered with a title and lyrics when applicable. It requires a ComfyUI server with AceStep Audio 1.5 installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Music tags and lyrics are sent to the configured ComfyUI endpoint, and generated audio is written locally.

Mitigation: Use a trusted endpoint and avoid sensitive inputs or shared output locations.

Risk: An undeclared background watcher can wait for a server and generate built-in songs without a current user request.

Mitigation: Review or remove _watch_and_generate.py before use; run only the requested music-generation workflow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/sunshinejnjn/skills/music-with-comfyui)
- [AceStep Audio 1.5 model](https://huggingface.co/AceStep/AceStep1.5)
- [Workflow attribution](references/attribution.md)
- [CLI usage reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Audio files, Text]

**Output Format:** [MP3 audio attachment with a Markdown title and optional lyrics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio is saved locally; channel-specific delivery may use another audio format or ZIP.]

## Skill Version(s):

0.3.0 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
