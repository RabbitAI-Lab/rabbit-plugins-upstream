## Description: <br>
SEO 博客写作基础版 helps an agent draft SEO-oriented blog content, including keyword-aware titles, meta descriptions, structured H2/H3 outlines, keyword variants, link suggestions, and image alt text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, personal bloggers, and content marketers use this skill to turn a topic or target keyword into SEO-ready blog structure and draft copy. It is aimed at lightweight single-user workflows rather than team or batch publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad command/tool access and includes an environment-variable check that may expose the names of sensitive credentials in a workspace. <br>
Mitigation: Review proposed shell commands before execution and avoid running broad environment-variable scans in sensitive workspaces. <br>
Risk: The skill may use external APIs or provider-backed agent tools for SEO content generation, which can transmit draft content or business context outside the local workspace. <br>
Mitigation: Confirm the active API provider and data handling terms before providing confidential drafts, credentials, customer data, or private business material. <br>
Risk: Generated SEO claims, titles, metadata, and content structure can be inaccurate, misleading, or unsuitable for publication without review. <br>
Mitigation: Have a human editor verify factual claims, search intent, keyword usage, links, and final copy before publishing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/blog-seo-writer-tool-free) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown or JSON with optional inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports json, text, and csv output preferences; free edition is described as single-task and non-batch.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
