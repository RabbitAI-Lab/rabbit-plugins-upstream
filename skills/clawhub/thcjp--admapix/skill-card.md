## Description: <br>
AdMapix fetches raw structured JSON from APIs for ad creatives, apps, rankings, distribution, market data, and estimated downloads and revenue. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, growth analysts, and agent users can use this skill to retrieve raw AdMapix advertising and app-market data for downstream analysis performed by the calling agent. It is intended for data access rather than autonomous research, summaries, recommendations, dashboards, or generated pages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security verdict is suspicious because the documentation asks for more authority than the read-only packaging suggests and contains conflicting scope and credential instructions. <br>
Mitigation: Install only when the user intends to let an agent call api.admapix.com with an AdMapix API key, and correct the command execution, file handling, and analysis/reporting documentation issues before broad deployment. <br>
Risk: The skill uses an AdMapix API key to access external data services. <br>
Mitigation: Configure the key through a secure host secret or environment variable, never paste it into chat, and avoid printing, logging, or storing the key. <br>
Risk: Download and revenue values are third-party estimates rather than official figures. <br>
Mitigation: Present those values as estimates and preserve the raw API response so downstream users can review the source fields. <br>


## Reference(s): <br>
- [AdMapix website](https://www.admapix.com) <br>
- [AdMapix API endpoint base](https://api.admapix.com/api/data/) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/admapix) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, API calls, Shell commands, Configuration guidance] <br>
**Output Format:** [Raw structured JSON from AdMapix APIs, with Markdown setup guidance and shell commands when authentication is missing.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ADMAPIX_API_KEY for direct API access; creative search page_size is capped at 10.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
