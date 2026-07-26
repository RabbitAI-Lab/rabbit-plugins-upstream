## Description: <br>
Searches synchronized Temu category records by keyword to find Chinese names, English names, and category IDs for Temu product or shop filtering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace users and agents use this skill when they need Temu category IDs from synchronized category data before filtering product or shop queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports a suspicious review concern because queries, API keys, and session metadata may be sent to a remote LinkFox gateway. <br>
Mitigation: Install only when the user accepts LinkFox gateway use, protect LinkFox API keys in environment variables, and avoid submitting sensitive category-search terms. <br>
Risk: The script may write or cache full response data under local linkfox directories. <br>
Mitigation: Review generated data files and cache locations after use, and remove stored responses when category results or session metadata should not persist. <br>
Risk: The skill depends on synchronized Temu category data, so results can be empty or stale if synchronization has not run recently. <br>
Mitigation: Run the documented Temu category synchronization before relying on search results for product or shop filtering. <br>


## Reference(s): <br>
- [Temu category API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-category-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API results and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses may be saved as JSON data files; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
