## Description:

Queries Steam and Epic Games libraries from local CLI tools, with Chinese-name cache support for listing, search, statistics, recommendations, and duplicate detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vlalamoon](https://clawhub.ai/user/vlalamoon)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect their own Steam and Epic Games libraries, find games by Chinese or English name, view library statistics, identify unplayed games, and get basic recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted search term could make the search command run unintended code.

Mitigation: Use only trusted, manually reviewed search terms until the search implementation safely passes user input.

Risk: The skill relies on logged-in local Steam and Epic tooling.

Mitigation: Run it only in a trusted local shell and review command output before sharing it outside the account owner context.

Risk: Chinese-name enrichment sends game identifiers to external Steam and Xiaoheihe endpoints.

Mitigation: Run name-cache update commands only when sharing game identifiers with those services is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vlalamoon/skills/game-library-publish)
- [Legendary CLI](https://github.com/derrod/legendary)
- [Steam Store app details API](https://store.steampowered.com/api/appdetails?appids={appid}&cc=cn&l=schinese)
- [Steam Store search API](https://store.steampowered.com/api/storesearch/?term={term}&l=schinese&cc=cn)
- [Xiaoheihe game detail endpoint](https://api.xiaoheihe.cn/game/share_game_detail)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal-oriented text with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local Steam and Legendary CLI access, STEAM_API_KEY, and optional Chinese-name cache files.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
