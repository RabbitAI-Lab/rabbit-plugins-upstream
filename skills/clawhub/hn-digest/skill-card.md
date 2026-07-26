## Description: <br>
Fetch and send Hacker News front-page posts on demand, then send a generated mood image inspired by the selected posts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cpojer](https://clawhub.ai/user/cpojer) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to request a concise Hacker News front-page digest by count or topic. The skill returns individual post messages and a generated image summarizing the mood of the selected stories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically generates an image after each digest, which may consume Gemini/Nano Banana or OpenAI quota. <br>
Mitigation: Review the skill before use, make image generation opt-in where possible, and run it with a dedicated limited API key. <br>
Risk: The image generation path can read provider credentials from environment variables or local OpenClaw configuration. <br>
Mitigation: Use scoped credentials and avoid exposing broad local configuration to the skill runtime. <br>
Risk: The helper script installs Python packages at runtime before generating images. <br>
Mitigation: Pin and review dependencies before deployment, or pre-build an isolated environment with approved package versions. <br>


## Reference(s): <br>
- [HN Digest on ClawHub](https://clawhub.ai/cpojer/skills/hn-digest) <br>
- [Hacker News](https://news.ycombinator.com/) <br>
- [HN Algolia Front Page API](https://hn.algolia.com/api/v1/search?tags=front_page) <br>
- [OpenAI Images API endpoint](https://api.openai.com/v1/images/generations) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, files] <br>
**Output Format:** [Individual text messages with title, age, comment count, and HN comment link, followed by a generated PNG image file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default count is 5 posts; supported topics are tech, health, hacking, life, and lifehacks; crypto posts are excluded.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
