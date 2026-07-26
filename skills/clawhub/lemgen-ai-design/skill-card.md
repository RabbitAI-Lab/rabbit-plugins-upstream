## Description: <br>
Search 4,500+ curated AI image and video prompts, enhance prompts, and generate with LemGen from OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aithink001](https://clawhub.ai/user/aithink001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and creative teams use this skill to search curated image and video prompt examples, refine or translate prompts, and optionally generate LemGen images or videos after approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow references a GitHub MCP package and uses a LemGen API token. <br>
Mitigation: Confirm the package is trusted before installing it and keep LEMGEN_API_TOKEN out of chat, logs, screenshots, and shared configuration. <br>
Risk: Image or video generation may consume paid LemGen resources, and video jobs may continue running after a timeout. <br>
Mitigation: Require explicit user approval before generation and check LemGen generation history before retrying failed or timed-out video jobs. <br>
Risk: Brand, celebrity, political, regulated-industry, copyrighted-character, or logo prompts can create misleading or rights-sensitive outputs. <br>
Mitigation: Keep prompts factual, avoid misleading claims, and use protected assets only when the user has the right to use them. <br>


## Reference(s): <br>
- [LemGen prompt gallery](https://lemgen.org) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [ClawHub skill page](https://clawhub.ai/aithink001/skills/lemgen-ai-design) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with prompt examples, JSON MCP configuration snippets, and tool-call recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generation tools require LEMGEN_API_TOKEN and explicit user approval; video generation can be slower and may use paid LemGen resources.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
