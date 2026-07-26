## Description: <br>
OpenClaw skill that provides a WordPress REST API CLI for posts, pages, categories, tags, users, and custom requests using plain HTTP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codedao12](https://clawhub.ai/user/codedao12) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation teams use this skill to operate WordPress content workflows through the REST API, including posts, pages, taxonomy, user reads, and custom requests. It is best suited for JSON-in/JSON-out pipelines where an agent needs explicit CLI commands and REST responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, publish, or delete WordPress content when configured with credentials that have write permissions. <br>
Mitigation: Use a dedicated low-privilege WordPress account, prefer draft status for staging content, and require explicit approval before create, update, publish, delete, or raw request actions. <br>
Risk: Misconfigured targets or credentials could send requests to the wrong WordPress site or expose access tokens. <br>
Mitigation: Set WP_BASE_URL only to the intended HTTPS site, keep application passwords and tokens out of logs and commits, and avoid passing secrets or unrelated local files through @file inputs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/codedao12/skills/wordpress) <br>
- [WordPress REST API Guide](artifact/assets/wordpress-rest-api-guide.md) <br>
- [Environment Example](artifact/env_example.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON responses from the WordPress REST API] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses environment variables for WordPress base URL and credentials; CLI errors return a non-zero exit code.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
