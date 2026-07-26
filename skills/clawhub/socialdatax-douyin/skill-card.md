## Description: <br>
SocialDataX Douyin helps agents perform read-only Douyin hot-search, content, comment, reply, creator profile, creator post, and short-drama series lookups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill for read-only Douyin content and creator research, including hot-search lookup, work discovery, detail lookup, comment analysis, reply lookup, creator profile lookup, creator work lists, and creator short-drama series lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SocialDataX API key to query Douyin data. <br>
Mitigation: Provide SOCIALDATAX_API_KEY through the environment, use the official SocialDataX access page, and avoid placing keys in skill files or prompts. <br>
Risk: Running the SocialDataX npm CLI, especially bulk options such as --all, may consume account credits or issue larger API requests. <br>
Mitigation: Review npm package provenance and SocialDataX billing or credit behavior before use, and start with scoped queries before bulk collection. <br>


## Reference(s): <br>
- [SocialDataX AI access](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and CLI or MCP tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY plus node and npm; CLI calls return read-only Douyin data through SocialDataX.] <br>

## Skill Version(s): <br>
0.1.15 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
