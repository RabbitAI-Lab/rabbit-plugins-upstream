## Description: <br>
文档导航服务 helps agents find ANSYS Fluent documentation through search suggestions, topic lists, and direct manual links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route ANSYS Fluent documentation questions to search, topic-listing, or direct manual-link tools and present the returned documentation links to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a XiaoBenYang API key and stores it locally in plaintext. <br>
Mitigation: Install only if the publisher and service are trusted; use a limited-scope key, avoid reusing secrets, and delete or rotate the key when uninstalling. <br>
Risk: Documentation answers depend on a third-party XiaoBenYang service before the skill can answer Fluent documentation questions. <br>
Mitigation: Review returned links before relying on them and avoid entering sensitive information into third-party documentation queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/fluent) <br>
- [XiaoBenYang API key service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, configuration] <br>
**Output Format:** [Markdown or plain text summaries of API-returned documentation URLs and navigation hints] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key before tool calls can return documentation results.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence; artifact frontmatter: 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
