## Description: <br>
Browse and search Hacker News, including story lists, item details, comments, user profiles, Algolia search, and "Who is hiring?" threads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gchapim](https://clawhub.ai/user/gchapim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and operators use this skill to browse Hacker News activity, inspect discussions, look up user profiles, search stories or comments, and find hiring threads from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, requested item IDs, and usernames are sent to external public Hacker News and Algolia APIs. <br>
Mitigation: Avoid sensitive private search terms and treat returned data as public web content. <br>
Risk: The CLI requires local curl, jq, and python3 to run successfully. <br>
Mitigation: Verify those dependencies are installed before relying on the skill in an agent workflow. <br>


## Reference(s): <br>
- [Hacker News API Reference](references/api.md) <br>
- [Hacker News Firebase API](https://hacker-news.firebaseio.com/v0/) <br>
- [Algolia Hacker News Search API](https://hn.algolia.com/api/v1/) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; command output is plain text or JSON when --json is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and python3; fetches public Hacker News and Algolia APIs without authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
