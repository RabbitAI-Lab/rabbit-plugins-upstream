## Description: <br>
Fetches current GitHub Trending repositories by daily, weekly, or monthly star growth through a standard-library Python scraper, with optional language filtering and JSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to answer questions about current GitHub repository trends and retrieve ranked trending projects for a selected period or programming language. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes live unauthenticated requests to public GitHub Trending pages when invoked, so results depend on network availability and GitHub's page structure. <br>
Mitigation: Use it only where live requests to GitHub are acceptable, retry transient network failures, and update the parser if GitHub changes the Trending page markup. <br>
Risk: The skill scrapes public web pages instead of using the GitHub API, so returned rankings can be incomplete or empty if parsing fails. <br>
Mitigation: Prefer JSON output for downstream processing and validate important results against GitHub Trending before relying on them in user-facing summaries. <br>


## Reference(s): <br>
- [GitHub Trending](https://github.com/trending) <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/github-trending-stable) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text list or JSON object, with shell command examples in documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results include repository rank, full name, URL, description, language, total stars, period star gain, and Beijing-time update timestamp when JSON output is requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
