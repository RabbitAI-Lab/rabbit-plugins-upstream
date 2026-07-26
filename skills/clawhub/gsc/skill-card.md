## Description: <br>
Query Google Search Console for SEO data, including search queries, top pages, CTR opportunities, URL inspection, and sitemaps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jdrhyne](https://clawhub.ai/user/jdrhyne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, marketers, and SEO analysts use this skill to query read-only Search Console data for properties they can access, inspect indexing status, list sitemaps, and find CTR or content optimization opportunities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth setup can print sensitive Google client secrets and refresh tokens. <br>
Mitigation: Run authentication in a private local terminal, avoid sharing logs or chat transcripts containing tokens, store secrets in a protected secret store or private environment file, and revoke exposed Google OAuth tokens. <br>


## Reference(s): <br>
- [Google Search Console documentation](https://developers.google.com/webmaster-tools) <br>
- [ClawHub Google Search Console skill](https://clawhub.ai/jdrhyne/skills/gsc) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; command output is text tables or JSON depending on the subcommand.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and Google OAuth environment variables. Search Console access is read-only, and reported data may lag by about three days.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
