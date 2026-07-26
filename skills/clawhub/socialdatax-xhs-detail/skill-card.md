## Description: <br>
Helps agents retrieve and summarize Xiaohongshu / XHS / RedNote note details, metrics, content, author, media, and related note data through SocialDataX. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to fetch read-only XHS note details by note ID or URL, then return structured facts such as title, content, author, publish time, interaction counts, images, and media summary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Returned XHS note URLs can include xsec_token query parameters that may appear in chat outputs, saved references, or forwarded results. <br>
Mitigation: Review where outputs are shared or stored before use, and only run the skill when preserving full tokenized note URLs is acceptable for the workspace. <br>
Risk: The skill sends note IDs or full note URLs to SocialDataX using SOCIALDATAX_API_KEY. <br>
Mitigation: Use a scoped SocialDataX API key from the user's environment and avoid submitting note URLs that should not be shared with the SocialDataX service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-detail) <br>
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub) <br>
- [Publisher profile](https://clawhub.ai/user/devinchen2014) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with factual note summaries, optional shell commands, and JSON returned by the SocialDataX CLI or MCP tools.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY for data calls and node/npm for the direct CLI path; optional media saving writes only to a requested local output path.] <br>

## Skill Version(s): <br>
0.1.14 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
