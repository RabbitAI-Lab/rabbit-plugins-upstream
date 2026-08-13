## Description:

当用户需要做抖音竞品研究、抖音竞品分析、同赛道观察、内容角度对比、内容策略对比或品牌内容调研时使用。面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Brand teams, MCNs, content operators, and creators use this skill to search Douyin by keyword and compare competitor content samples, topics, account signals, and strategy angles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches and API-key-authenticated requests are sent to the external SocialDataX service through the npm package.

Mitigation: Confirm trust in SocialDataX and the socialdatax-skills npm package before installation, and provide SOCIALDATAX_API_KEY only in environments where that service use is approved.

Risk: The local environment may lack Node.js, npm, npx, network access, or execution permission needed for the direct CLI workflow.

Mitigation: Check the required node and npm binaries before use, then retry the documented command after installing dependencies or granting network and execution access.

Risk: Competitor research conclusions may be misleading if returned Douyin samples are sparse, over-filtered, or not preserved with traceable evidence.

Mitigation: Keep visible evidence separate from judgment, preserve useful content IDs, links, titles, author names, metrics, publish times, and content types, and broaden keywords or filters when results are thin.

## Reference(s):

- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/douyin-competitor-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-backed search result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Douyin content IDs, links, titles, author or account names, metrics, publish times, content types, and next-step analysis questions when available.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
