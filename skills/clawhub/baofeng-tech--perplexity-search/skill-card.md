## Description: <br>
Perplexity Sonar search and answer generation through AIsa for citation-backed web answers, analytical reasoning, and long-form research reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baofeng-tech](https://clawhub.ai/user/baofeng-tech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they need Perplexity Sonar, Sonar Pro, Sonar Reasoning Pro, or Sonar Deep Research through AIsa for citation-backed web answers, analytical reasoning, comparison work, or longer research reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user search prompts to AIsa Perplexity endpoints using AISA_API_KEY. <br>
Mitigation: Use it only with queries and data that are acceptable under the user's AIsa account and data policy, and avoid including secrets or private data in prompts. <br>
Risk: Sonar Deep Research requests may be slow or time out. <br>
Mitigation: Narrow the query, retry later, or use sonar-pro or sonar-reasoning-pro when a faster response is needed. <br>


## Reference(s): <br>
- [ClawHub Perplexity Search release](https://clawhub.ai/baofeng-tech/skills/perplexity-search) <br>
- [AIsa](https://aisa.one) <br>
- [AIsa Sonar API reference](https://aisa.one/docs/api-reference/perplexity/post_perplexity-sonar) <br>
- [AIsa Sonar Pro API reference](https://aisa.one/docs/api-reference/perplexity/post_perplexity-sonar-pro) <br>
- [AIsa Sonar Reasoning Pro API reference](https://aisa.one/docs/api-reference/perplexity/post_perplexity-sonar-reasoning-pro) <br>
- [AIsa Sonar Deep Research API reference](https://aisa.one/docs/api-reference/perplexity/post_perplexity-sonar-deep-research) <br>
- [Agent Skills specification](https://agentskills.io/specification) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3, AISA_API_KEY, and network access to AIsa Perplexity endpoints; deep research requests may take longer and can time out.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
