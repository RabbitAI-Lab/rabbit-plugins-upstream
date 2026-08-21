## Description:

kurobbs-wiki helps agents query Wuthering Waves wiki entries, strategy posts, character profiles, and team-building recommendations from Kuro BBS, with optional account login for user-owned character analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alphamancer](https://clawhub.ai/user/alphamancer)

### License/Terms of Use:

MIT

## Use Case:

External users and agent developers use this skill to answer Wuthering Waves wiki and strategy questions, fetch structured or rendered entry details, and generate team-building guidance from public Kuro BBS data. Users who choose to log in can analyze their own Kuro BBS character roster locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional account features store Kuro BBS phone, token, and character data locally in plaintext.

Mitigation: Prefer public wiki commands when account-specific analysis is unnecessary, and delete ~/.kurobbs-wiki-cache/account.json when account features are no longer needed.

Risk: Community post media fetching can automate a browser against Kuro BBS site protections.

Mitigation: Run post/media commands only for user-requested posts and review the command, destination directory, and downloaded files before further processing.

Risk: Media download and video processing can invoke Playwright and ffmpeg on external content.

Mitigation: Keep media work in a temporary directory, process only expected image/video outputs, and remove downloaded media after use.

## Reference(s):

- [Server-resolved source repository](https://github.com/Alphamancer/kurobbs-wiki)
- [ClawHub skill page](https://clawhub.ai/alphamancer/skills/kurobbs-wiki)
- [Catalogue map](references/catalogue-map.md)
- [English README](README.en.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and human-readable CLI output, with optional structured JSON and local media file references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public wiki commands do not require login; optional account features cache Kuro BBS phone, token, and character data locally.]

## Skill Version(s):

0.1.0 (source: frontmatter, _meta.json, and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
