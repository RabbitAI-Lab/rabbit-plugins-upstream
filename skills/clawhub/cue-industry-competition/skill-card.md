## Description:

用 Cue 穿透目标行业的景气周期、竞争格局与产业链地位，识别集中度、龙头壁垒与供需或政策拐点，研判当前所处周期位置与投资机会窗口，产出可支撑配置决策的行业研判底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and investment researchers use this skill to run Cue-based industry research for cycle positioning, competitive landscape assessment, supply-demand inflection analysis, policy catalysts, industry-chain position, and investment-window judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an unpinned external Cue runner and Cue service, which can change behavior, fail, or expose prompts and generated reports to Cue.

Mitigation: Use a pinned and reviewed runner version, run the documented health checks before use, and limit use to non-sensitive research prompts unless Cue data sharing is acceptable.

Risk: The skill pushes share links and commercial account actions by default, including report URLs and payment or credit flows.

Mitigation: Review generated report links before sharing, avoid entering sensitive content, and confirm account or credit actions with the user before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-industry-competition)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue Playbook API](https://cuecue.cn/api/playbook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown research report with source links, plus Cue runner commands and a Cue share URL when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a local Markdown report file under ~/cue-reports when the Cue runner succeeds.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
