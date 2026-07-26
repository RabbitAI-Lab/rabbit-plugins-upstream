## Description: <br>
Searches and analyzes trending GitHub repositories by topic, star count, creation date, programming language, and sort order. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manifoldor](https://clawhub.ai/user/manifoldor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and technical researchers use this skill to discover popular or recently created open-source GitHub repositories that match specific topics, languages, star thresholds, and freshness criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A configured GITHUB_TOKEN could expose unnecessary repository access if it has broad scopes or is stored permanently in a shell profile. <br>
Mitigation: Use the least privilege needed, avoid private-repository and write scopes, treat the token as a secret, and prefer a temporary environment variable or secret manager over saving it in ~/.zshrc. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/manifoldor/skills/explorer) <br>
- [GitHub Search API reference](references/github_api.md) <br>
- [GitHub REST Search documentation](https://docs.github.com/en/rest/search) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Terminal text and Markdown-style command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Repository summaries include names, descriptions, URLs, stars, forks, language, tags, and created or updated dates; optional GITHUB_TOKEN configuration can increase GitHub API rate limits.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
