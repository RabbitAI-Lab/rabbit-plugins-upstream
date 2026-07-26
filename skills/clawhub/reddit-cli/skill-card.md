## Description: <br>
Reddit CLI using cookies for authentication. Read posts, search, and get subreddit info. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kelsia14](https://clawhub.ai/user/kelsia14) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users can use this skill to run Reddit CLI commands that fetch subreddit posts, search Reddit, inspect subreddit metadata, and check cookie-based connectivity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses live Reddit session cookies for authentication. <br>
Mitigation: Treat REDDIT_SESSION and TOKEN_V2 like passwords, avoid storing them in shared shell startup files, and rotate or log out of Reddit if the values may have leaked. <br>
Risk: Persisting Reddit cookies in shell configuration can expose them to other local users, backups, or accidental commits. <br>
Mitigation: Prefer a temporary shell environment or secret manager, and do not commit files containing these values. <br>


## Reference(s): <br>
- [Reddit](https://reddit.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/kelsia14/skills/reddit-cli) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/kelsia14) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain terminal text with command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses REDDIT_SESSION and optional TOKEN_V2 environment variables supplied by the user.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
