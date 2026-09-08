## Description:

Evaluates WeChat Channel creators before ad placement by locating accounts, retrieving recent videos and interaction metrics, and producing a recommendation-oriented audit report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, agencies, and operators use this skill before WeChat Channel ad placements or creator collaborations to assess audience activity, content performance, and whether an account is worth sponsoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a ManGeYun/We-Media API key and can make paid API calls after user confirmation.

Mitigation: Review the printed cost estimate before adding --yes, monitor account balance, and avoid running paid endpoints without explicit approval.

Risk: The skill writes configuration, cache, and report files locally.

Mitigation: Store the API key only in approved locations and review generated output and cache files before sharing or retaining them.

Risk: The security evidence flags under-disclosed local-file upload behavior and bundled bytecode.

Mitigation: Do not pass local file paths or --file unless upload behavior is explicitly approved; review source and bytecode contents before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-channel-ad-audit)
- [We-Media API site](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown, JSON, Excel files, and shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports local output file paths, row counts, estimated and actual CNY consumption, and remaining account balance.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence; artifact frontmatter reports v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
