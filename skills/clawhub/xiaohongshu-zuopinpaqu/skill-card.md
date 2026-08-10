## Description: <br>
Searches Xiaohongshu public posts by keyword, fetches note details and comments, and retrieves a creator's public posts as structured results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[engheng-art](https://clawhub.ai/user/engheng-art) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External marketers, content operators, analysts, and agents use this skill to collect public Xiaohongshu keyword results, note comments, and creator post lists for content research, competitive monitoring, trend tracking, and reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided Xiaohongshu keywords, note URLs, profile URLs, and related xsec_token query strings are sent to the Guaikei API. <br>
Mitigation: Use only public, shareable search terms and links, and avoid confidential research terms, private target lists, or links containing parameters that should not be shared. <br>
Risk: Returned public-data results may be saved locally under logs/. <br>
Mitigation: Review generated logs before sharing or retaining them, and remove outputs that should not be stored. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xiaohongshu-zuopinpaqu) <br>
- [Guaikei API service](https://www.guaikei.com) <br>
- [Options reference](references/options.md) <br>
- [Changelog](references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance, files] <br>
**Output Format:** [JSON command output with concise Markdown guidance and local JSON result logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save result logs locally under logs/.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, release evidence, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
