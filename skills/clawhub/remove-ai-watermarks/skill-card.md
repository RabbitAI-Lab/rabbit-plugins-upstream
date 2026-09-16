## Description:

Removes and identifies AI watermarks and provenance marks in images and video the user generated or edited.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect or remove local AI provenance marks from images and videos they generated, edited, and are allowed to change. It routes agents through probing, installation checks, identification, removal commands, and cautious reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to install or replace a third-party CLI package during use.

Mitigation: Require explicit confirmation before install or upgrade, prefer an isolated environment, and pin the reviewed package version.

Risk: Watermark or provenance removal can be misused to alter content the user is not allowed to modify or to make deceptive origin claims.

Mitigation: Use only on content the user generated or edited and is allowed to change; refuse third-party paid-asset watermark removal and deceptive human-made origin claims.

Risk: Local removal or identification results can be overstated as proof that a file is human-made or clean.

Mitigation: Report only what the command actually did, preserve caveats, and avoid claiming that local signal absence proves content origin.

## Reference(s):

- [Install Extras](references/install.md)
- [Command Recipes](references/commands.md)
- [Project Homepage](https://raiw.cc)
- [Repository Metadata Link](https://github.com/wiltodelta/remove-ai-watermarks)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, configuration]

**Output Format:** [Markdown with inline shell commands and concise status reporting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference command exit codes, probe JSON, output paths, and install guidance.]

## Skill Version(s):

1.0.9 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
