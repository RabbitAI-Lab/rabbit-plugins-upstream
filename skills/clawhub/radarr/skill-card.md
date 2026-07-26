## Description: <br>
Search and add movies to Radarr, including collections and optional search-on-add behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jordyvandomselaar](https://clawhub.ai/user/jordyvandomselaar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
People who run a Radarr media library use this skill to search for movies, add individual titles or collections, check whether movies already exist, and remove movies through Radarr's API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Removing a movie with the delete-files option can delete media from disk. <br>
Mitigation: Confirm the exact movie and require explicit user intent before using delete-files. <br>
Risk: Adding a collection can enable monitoring and future automatic additions. <br>
Mitigation: Tell the user that collection monitoring may add future releases before running add-collection. <br>
Risk: The skill controls a Radarr library through an API key. <br>
Mitigation: Use a Radarr API key only in the expected local credentials file and limit access to trusted users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jordyvandomselaar/skills/radarr) <br>
- [Publisher profile](https://clawhub.ai/user/jordyvandomselaar) <br>
- [The Movie Database movie links](https://themoviedb.org/movie/ID) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and shell command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq, plus a local Radarr URL, API key, and default quality profile configuration.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
