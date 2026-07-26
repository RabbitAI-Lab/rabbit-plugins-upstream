## Description: <br>
Fetches Reddit post comment threads via Reddit's public JSON API and returns flat JSON comment records with pagination support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and automation users use this skill to collect comments and nested replies from Reddit posts for downstream review, analysis, or workflow processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses shell eval command templates to execute generated JavaScript. <br>
Mitigation: Review generated commands before execution and prefer a safer invocation path that validates parameters without shell eval. <br>
Risk: The skill performs direct Reddit API requests and may use the active browser session context. <br>
Mitigation: Disclose network access before use and run it only for Reddit content the user is authorized to access. <br>
Risk: Anonymous Reddit API access may be rate limited during large comment collection jobs. <br>
Mitigation: Batch morechildren requests serially and add the documented delay between batches. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/reddit-post-comments) <br>
- [Publisher Profile](https://clawhub.ai/user/browseract-cli) <br>
- [Reddit Comments JSON Endpoint](https://www.reddit.com/comments/) <br>
- [Reddit Morechildren API](https://www.reddit.com/api/morechildren.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with bash command templates that return JSON comment data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns flat comment arrays, pagination IDs, counts, error objects, and per-comment metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
