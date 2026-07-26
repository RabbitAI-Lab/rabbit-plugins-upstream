## Description: <br>
Searches for movies by genre, year, rating, or title in Chinese or English and can generate a local HTML page with embedded third-party playback sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chugenice](https://clawhub.ai/user/chugenice) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search movie metadata, compare candidate results, and produce a playback-oriented HTML page after a movie is selected. It is intended for entertainment discovery workflows and should be limited to authorized media sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated playback pages may load unvetted third-party streaming embeds that expose browser or IP data, show unsafe content, or raise copyright and legal concerns. <br>
Mitigation: Prefer metadata-only results or authorized streaming providers, and require explicit user confirmation before generating any playback page. <br>
Risk: Fallback web searches can discover arbitrary embed URLs when trusted metadata or identifiers are unavailable. <br>
Mitigation: Restrict fallback sources to allowlisted providers and avoid embedding URLs that cannot be verified as authorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chugenice/skills/movie-finder) <br>
- [Publisher profile](https://clawhub.ai/user/chugenice) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown-style search results plus generated HTML playback pages and optional Python command invocations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local HTML files containing iframe embeds for third-party streaming sources.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
