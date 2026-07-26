## Description: <br>
Monitors GitHub Trending and tech communities to track and analyze emerging tools in CLI, AI/ML, automation, and developer categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guogang1024](https://clawhub.ai/user/guogang1024) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use Trend Watcher to monitor public GitHub repository trends, filter projects by language and category, generate trend reports, and bookmark projects for later review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bookmarks may persist in a hard-coded local workspace file. <br>
Mitigation: Use the bookmark feature only when local persistence is intended, and review or clear the bookmark file during workspace cleanup. <br>
Risk: Reports can include untrusted public repository names and descriptions from GitHub. <br>
Mitigation: Treat repository descriptions as public third-party content and review projects before acting on recommendations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/guogang1024/skills/trend-watcher) <br>
- [GitHub Trending](https://github.com/trending) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Guidance] <br>
**Output Format:** [Console trend report or JSON analysis, with optional bookmark data written as JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public GitHub Trending data when available and cached sample data when the network request fails.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
