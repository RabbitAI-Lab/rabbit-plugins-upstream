## Description: <br>
央视新闻抓取(免费版) helps an agent retrieve CCTV News content for a specified date, classify basic domestic and international items, and produce a concise news brief. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users, content creators, and developers use this skill to ask an agent for a dated CCTV News lookup, receive structured title and summary data, and generate a lightweight brief for review or downstream processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags broad activation wording and an unverified remote installer recommendation. <br>
Mitigation: Invoke the skill only for explicit CCTV News date queries, review installation steps first, and avoid automatic curl-to-shell execution. <br>
Risk: The skill can direct an agent to run shell commands and install runtime dependencies. <br>
Mitigation: Review proposed commands and package installation steps before execution, and run them only in an environment where Node.js, Bun, and npm dependencies are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cctv-news-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell and code examples, plus JSON-style news data and text briefs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are scoped to single-date news retrieval in the free edition; batch queries, AI summaries, push delivery, trend analysis, full-text content, and video metadata are listed as unavailable.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
