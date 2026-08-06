## Description:

Power-user guide to always getting top-tier frontier models on Arena.ai with Max router, Direct vs Agent vs Code selection, rotation caveats, Pineapple mitigation 3-strike, 5-message chunking, local fallback matrix with edge-cpu-gguf-tuner and sandbox-selfheal-guard when Arena down.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this reference playbook to choose Arena.ai modes, route through Max, recover from weak responses, and fall back to configured local tools when Arena is unavailable or throttled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional local fallback and caching commands may run separately installed tools or retain prompt and response content in /tmp.

Mitigation: Run those commands only for trusted local tools and avoid caching sensitive prompts or responses unless local retention is acceptable.

Risk: The playbook may contain time-sensitive model-routing and frontier-model guidance that can become stale.

Mitigation: Treat the guidance as a reference and verify current Arena.ai routing, model availability, and fallback behavior before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/arena-power-user-playbook)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [Arena.ai](https://arena.ai/)
- [Arena Agent Mode](https://arena.ai/agent)
- [Arena Agent Leaderboard](https://arena.ai/leaderboard/agent)
- [Arena Max](https://arena.ai/max)
- [Arena Agent Mode blog](https://arena.ai/blog/agent-mode/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with decision guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference playbook; optional commands depend on separately installed local fallback tools.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
