## Description: <br>
获取微博实时热搜榜，返回热搜词、热度及话题链接。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve the current Weibo hot-search list through TianAPI and present trend words, heat scores, tags, and topic links to an agent user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A TianAPI account key is required and can be exposed if passed on the command line, placed in a checked-in .env file, or shown in screenshots. <br>
Mitigation: Prefer the TIANAPI_WEIBO_HOT_KEY environment variable, keep any .env file out of source control, avoid sharing command histories or screenshots containing the key, and rotate the key if exposure is suspected. <br>
Risk: The skill depends on live TianAPI and Weibo trend data, so results can be unavailable, quota-limited, or time-sensitive. <br>
Mitigation: Handle TianAPI error codes and network timeouts as user-visible failures, and treat returned hot-search data as current-at-request-time rather than durable reference data. <br>
Risk: The artifact script behavior should be validated before operational use because the script body has inconsistencies between documented CLI behavior and implemented arguments/method names. <br>
Mitigation: Run a smoke test with a non-sensitive TianAPI key in a controlled environment and correct script invocation issues before relying on automated agent execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/workxin/skills/tianapi-weibo-hot) <br>
- [TianAPI Weibo Hot API Documentation](https://www.tianapi.com/apiview/100) <br>
- [TianAPI Weibo Hot API Endpoint](https://apis.tianapi.com/weibohot/index) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Console text list or JSON data describing Weibo hot-search topics, heat scores, tags, and links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, network access to TianAPI, and a TIANAPI_WEIBO_HOT_KEY API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
