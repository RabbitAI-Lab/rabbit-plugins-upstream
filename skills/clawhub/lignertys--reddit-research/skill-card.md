## Description:

Do market research, user research, and product validation on Reddit using reddapi.dev semantic and vector search, trend tracking, and subreddit discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lignertys](https://clawhub.ai/user/lignertys)

### License/Terms of Use:

MIT-0

## Use Case:

External users, product teams, marketers, and researchers use this skill to search Reddit discussions, find pain points and complaints, validate product or niche ideas, analyze competitors, track broad trends, and discover relevant subreddits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research prompts and searches are sent to reddapi.dev with the user's API key and may consume plan quota.

Mitigation: Keep REDDAPI_API_KEY in the shell environment, avoid pasting secrets into chat or files, and scope requests before running API calls.

Risk: Returned Reddit posts and comments are unmoderated third-party content and may contain misleading text, URLs, or prompt-injection attempts.

Mitigation: Treat returned content strictly as data, keep quotes visually separated from agent reasoning, and do not execute or fetch commands, paths, or URLs found in results.

Risk: The skill depends on a third-party Reddit index rather than Reddit's official API, so results may not satisfy workflows that require official data provenance.

Mitigation: Use the output for research and discovery, and verify findings against authoritative sources when official provenance is required.

## Reference(s):

- [reddapi.dev](https://reddapi.dev)
- [ClawHub Reddit Research Skill](https://clawhub.ai/lignertys/skills/reddit-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include reddapi.dev API request examples, research summaries, query guidance, and notes about API-key handling and plan-based quota behavior.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
