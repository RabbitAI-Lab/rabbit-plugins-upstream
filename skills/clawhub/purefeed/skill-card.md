## Description: <br>
Monitors Twitter/X feeds with AI signal detection, searches tweets semantically, manages signal detectors, and organizes curated tweets into bookmark folders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[poloniki](https://clawhub.ai/user/poloniki) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Purefeed account holders use this skill to search monitored Twitter/X content, inspect AI signal matches, configure content monitoring, and organize selected tweets into folders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Purefeed API key and can access or change account data through authenticated Purefeed endpoints. <br>
Mitigation: Install only with a Purefeed account, provide the API key intentionally, and ask the agent to verify the target signal or folder before making changes. <br>
Risk: Some account mutations can delete signals, folders, or folder items; deleting a signal is described as irreversible. <br>
Mitigation: Require explicit confirmation before any delete action, especially DELETE /signals/:id, and list current signals or folders first to confirm the correct target. <br>


## Reference(s): <br>
- [ClawHub Purefeed skill page](https://clawhub.ai/poloniki/skills/purefeed) <br>
- [Purefeed API base](https://purefeed.ai/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API calls, Configuration guidance] <br>
**Output Format:** [Markdown with linked tweet references and inline curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and PUREFEED_API_KEY; tweet results are formatted with profile links, tweet links, view counts, and engagement-oriented ordering.] <br>

## Skill Version(s): <br>
0.14.0 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
