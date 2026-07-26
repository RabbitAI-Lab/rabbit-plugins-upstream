## Description: <br>
Analyzes TikTok Shop products through the ClawEC API, including channel mix, content format, paid versus organic traffic, daily trends, and optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, ecommerce researchers, and agent operators use this skill to submit TikTok Shop product IDs or links to ClawEC and summarize product performance, traffic mix, content distribution, trends, and optional AI interpretation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a ClawEC API key to call third-party endpoints. <br>
Mitigation: Keep CLAWEC_API_KEY secret, prefer environment variables, and do not hard-code or expose the key in prompts, logs, or shared output. <br>
Risk: Submitted product IDs or links and related lookup history are sent to and processed by ClawEC. <br>
Mitigation: Use the skill only for product data that the user is permitted to send to ClawEC and disclose that the lookup is processed by ClawEC. <br>
Risk: Optional AI interpretation may still be processing, fail, or time out. <br>
Mitigation: Return available raw analysis data, report the AI status clearly, and retry the detail lookup later when appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-tiktok-product-analysis) <br>
- [ClawEC API base URL](https://www.clawec.com/api) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown summary with optional JSON API results and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-supplied CLAWEC_API_KEY, a TikTok Shop product ID or link, an optional region code, and optional AI interpretation polling.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
