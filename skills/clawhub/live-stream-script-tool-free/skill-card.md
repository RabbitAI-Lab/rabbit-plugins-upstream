## Description: <br>
为个人主播与内容创作者生成直播脚本，包括开场白、产品介绍、互动话题和结尾话术。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, individual livestream hosts, and content operators use this skill to draft structured livestream scripts for ecommerce, knowledge sharing, entertainment, and gaming sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill metadata declares read, write, and exec tool access even though the artifact is mostly Markdown guidance. <br>
Mitigation: Run it in normal agent sessions with command and file-change review enabled, and approve file or shell actions only when they match the livestream script task. <br>
Risk: Generated livestream scripts may contain promotional claims or conversion language that is inaccurate or unsuitable for the product or audience. <br>
Mitigation: Have a human reviewer verify factual product claims, pricing, compliance language, and platform policy fit before using the script live. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown and structured text, with optional JSON-style response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces draft livestream scripts, speaking prompts, pacing guidance, and template-style configuration examples for human review.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
