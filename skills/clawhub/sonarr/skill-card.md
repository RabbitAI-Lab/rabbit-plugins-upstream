## Description: <br>
Searches for and adds TV shows to a Sonarr library, with monitor options and search-on-add support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jordyvandomselaar](https://clawhub.ai/user/jordyvandomselaar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users with a configured Sonarr instance use this skill to search for TV shows, check library status, add monitored series, and remove existing series when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can remove Sonarr library entries and can delete media files when --delete-files is used. <br>
Mitigation: Ask for explicit user approval before remove actions, especially --delete-files, and confirm the selected TVDB ID and show title. <br>
Risk: A misconfigured Sonarr URL or exposed API key could let an agent manage the wrong Sonarr instance or disclose credentials. <br>
Mitigation: Verify the configured URL points to the intended Sonarr instance and protect ~/.clawdbot/credentials/sonarr/config.json. <br>
Risk: Adding a show changes the Sonarr library and can immediately start searches for missing episodes. <br>
Mitigation: Confirm the chosen search result, quality profile, and search-on-add preference before running add commands. <br>


## Reference(s): <br>
- [ClawHub Sonarr skill page](https://clawhub.ai/jordyvandomselaar/skills/sonarr) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands, plus text or JSON output from the Sonarr API wrapper.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and a Sonarr configuration file containing URL, API key, and optional default quality profile; search output is limited to 10 results.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
