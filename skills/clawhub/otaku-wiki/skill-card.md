## Description: <br>
Otaku Wiki helps agents answer anime, character, and voice actor questions in Chinese by querying AniList through a bundled Python CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robin797860](https://clawhub.ai/user/robin797860) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent developers use this skill to retrieve AniList-backed encyclopedia details for anime, characters, and staff, then present concise Chinese answer cards with source links. It supports direct lookups, search fallback, and anime comparison summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends anime, character, or staff search terms to AniList. <br>
Mitigation: Avoid entering private or sensitive text in lookup queries. <br>
Risk: The skill runs a bundled Python script during lookup. <br>
Mitigation: Review and scan the skill before deployment, and run it only where outbound AniList requests are acceptable. <br>


## Reference(s): <br>
- [AniList GraphQL API](https://graphql.anilist.co) <br>
- [ClawHub Skill Page](https://clawhub.ai/robin797860/skills/otaku-wiki) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Chinese Markdown answer cards backed by JSON lookup results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses AniList search results and source links; no local database is required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
