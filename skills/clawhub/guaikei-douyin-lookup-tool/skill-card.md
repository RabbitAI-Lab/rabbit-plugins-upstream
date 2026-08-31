## Description:

This skill helps agents collect public Douyin search results, creator posts, comments, and hot-list data as structured JSON for content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content research teams use this skill to query public Douyin data for short-video content planning, competitor monitoring, public comment analysis, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad short-video research prompts may trigger the skill and send search terms, Douyin URLs, comment datasets, and the GUAIKEI token to the provider.

Mitigation: Review the intended query and target before execution, avoid sensitive research targets, and confirm ambiguous prompts before invoking the skill.

Risk: Large public-data results and query details may be saved locally under logs.

Mitigation: Treat generated logs as sensitive research artifacts, delete them when no longer needed, and avoid storing private or regulated information in prompts or query inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-lookup-tool)
- [README](readme.md)
- [CLI options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot-list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON on stdout, diagnostic logs on stderr, and optional saved JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js 16.14 or newer; single requests can return up to 10000 records.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, references/changelog.md, src/config/constants.js)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
