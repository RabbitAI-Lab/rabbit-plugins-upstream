## Description: <br>
Red Note Content Topic is an AI-powered Xiaohongshu (RED) topic planner that generates trending topic ideas and title directions from account positioning and target audience details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wsd-mj](https://clawhub.ai/user/wsd-mj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, marketers, and social media operators use this skill to generate Xiaohongshu (RED) topic ideas and headline directions from account positioning and optional audience details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a WSD_API_KEY and sends account positioning plus optional audience details to wsdsocial.com. <br>
Mitigation: Store the API key in an environment variable, restrict access to the key, and avoid sending confidential business or audience strategy details unless approved. <br>
Risk: Generated topic and headline suggestions may be inaccurate, off-brand, or unsuitable for a target audience. <br>
Mitigation: Review suggestions before publication and apply brand, legal, and platform-policy checks. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/WSD-MJ/red-note-content-topic) <br>
- [ClawHub skill page](https://clawhub.ai/wsd-mj/skills/red-note-content-topic) <br>
- [WSD Social skill access](https://ai.wsdsocial.com/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Text or Markdown response with topic suggestions and headline ideas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WSD_API_KEY and uses account_direction plus optional target_audience inputs.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
