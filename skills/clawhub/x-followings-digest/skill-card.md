## Description: <br>
Auto-fetch latest tweets from X/Twitter followings and generate a structured AI digest for 1-day, 3-day, 7-day, or custom time ranges. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kaima2022](https://clawhub.ai/user/kaima2022) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to fetch tweets from followed X/Twitter accounts with their own session credentials and turn them into structured daily, weekly, or custom-range digests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses X/Twitter session credentials, so AUTH_TOKEN and CT0 exposure could allow unauthorized account access. <br>
Mitigation: Treat AUTH_TOKEN and CT0 like passwords and keep them out of shell history, dotfiles, logs, screenshots, and shared environments. <br>
Risk: Fetched tweets and generated digests may reveal private reading habits or followed-account activity. <br>
Mitigation: Protect generated tweet and digest files, and delete them when they are no longer needed. <br>
Risk: Recurring cron use can repeatedly fetch authenticated X/Twitter data without further prompts. <br>
Mitigation: Enable cron only when recurring fetching is intentional and review local storage permissions for generated outputs. <br>
Risk: The workflow depends on the local bird CLI for authenticated fetching. <br>
Mitigation: Install and run the skill only on a trusted machine with a trusted bird CLI. <br>


## Reference(s): <br>
- [AI Digest Analyst Prompt Template](references/analyst_prompt_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and a digest prompt template; tweet fetching returns JSON from the shell script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports tweet limit and day-range arguments; digest language can be Chinese, English, or bilingual.] <br>

## Skill Version(s): <br>
1.1.1 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
