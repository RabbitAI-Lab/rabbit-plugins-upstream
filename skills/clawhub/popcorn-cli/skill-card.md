## Description: <br>
Popcorn CLI helps agents use the local popcorn-cli command to submit Popcorn image or video tasks, list available models, and check task status with a locally configured API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zeyiy](https://clawhub.ai/user/zeyiy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill in terminal, scripting, CI, or automation workflows to submit Popcorn image and video tasks, inspect available model schemas, and query results by session or task ID. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A persistent backend URL override could redirect API-key-authenticated requests and task payloads. <br>
Mitigation: Use `popcorn-cli config show` to verify the configured backend before use, and treat any `config set-url` change as a sensitive trust decision. <br>
Risk: The local API key configuration can expose Popcorn account access if shared or leaked. <br>
Mitigation: Keep `~/.popcorn-cli/config.json` private, avoid shared machines, and rotate the API key if the file may have been exposed. <br>
Risk: Submitted prompts, media parameters, or business data are sent to the configured Popcorn backend. <br>
Mitigation: Do not submit confidential data unless the Popcorn service, configured endpoint, and data-handling terms are approved for that use. <br>


## Reference(s): <br>
- [Popcorn CLI Installation Guide](https://mangaforge-qa-1255521909.cos.ap-shanghai.myqcloud.com/docs/popcorn-cli/popcorn-cli-installation-guide.html) <br>
- [ClawHub Popcorn CLI Skill](https://clawhub.ai/zeyiy/skills/popcorn-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the popcorn-cli binary and a private local configuration file at ~/.popcorn-cli/config.json.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and release changelog; artifact frontmatter says 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
