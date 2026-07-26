## Description: <br>
Manage Readwise highlights, books, daily review, and Reader documents for saving URLs, browsing reading lists, searching documents, reviewing highlights, and managing notes through the Readwise and Reader APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gchapim](https://clawhub.ai/user/gchapim) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to interact with Readwise and Reader accounts: saving articles, listing or searching documents, creating and updating highlights, reviewing daily highlights, and managing books or tags. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, change, and delete items in a user's Readwise or Reader account when given an API token. <br>
Mitigation: Install only when this account access is acceptable, treat READWISE_TOKEN like a password, and use the skill only for explicit Readwise or Reader tasks. <br>
Risk: Update and delete commands can affect the wrong document or highlight if an incorrect ID is used. <br>
Mitigation: Verify the exact document or highlight ID before any update or delete operation. <br>


## Reference(s): <br>
- [Readwise & Reader API Reference](references/api.md) <br>
- [Readwise API token page](https://readwise.io/access_token) <br>
- [Readwise API v2](https://readwise.io/api/v2) <br>
- [Reader API v3](https://readwise.io/api/v3) <br>
- [ClawHub skill page](https://clawhub.ai/gchapim/skills/readwise-api) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and a READWISE_TOKEN environment variable; API responses can be compact JSON or pretty-printed JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
