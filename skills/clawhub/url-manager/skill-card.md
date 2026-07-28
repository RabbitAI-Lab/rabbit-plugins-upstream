## Description: <br>
URL Manager helps agents save, organize, search, and share web links and notes through a hosted card-based collection service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[piccolo123](https://clawhub.ai/user/piccolo123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to collect URLs or text notes, organize them into categories and tags, search saved items, and share curated collections through the hosted ai.ocean94.com service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically create an account and store saved URLs, notes, categories, tags, and sharing metadata on ai.ocean94.com. <br>
Mitigation: Inform the user before first save or search, confirm they accept the hosted data flow, and direct them to the service for data management or deletion. <br>
Risk: The skill stores a bearer token in a local .token file and can generate login or invite links that function like credentials. <br>
Mitigation: Treat the .token file and generated links as sensitive credentials, avoid sharing them in public channels, and rotate or re-register only when the user understands that it may create a new account. <br>
Risk: Shared category changes, invite links, and cocreate actions can affect other members' access or shared collections. <br>
Mitigation: Ask for user confirmation before creating shared categories, generating invite links, modifying cocreate categories, or removing items from shared categories. <br>
Risk: The fallback instructions clone a repository path when the script is missing, which evidence security guidance flags as needing trust in that source. <br>
Mitigation: Prefer the bundled script from the installed skill and avoid the fallback clone path unless the user explicitly trusts the repository source. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/piccolo123/skills/url-manager) <br>
- [Hosted URL Manager service](https://ai.ocean94.com) <br>
- [User Agreement](https://ai.ocean94.com/terms.html) <br>
- [Privacy Policy](https://ai.ocean94.com/privacy.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and network access to ai.ocean94.com; commands may create a local bearer token file and send saved URL, note, category, tag, and sharing data to the hosted service.] <br>

## Skill Version(s): <br>
2.6.3 (source: server evidence release version and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
