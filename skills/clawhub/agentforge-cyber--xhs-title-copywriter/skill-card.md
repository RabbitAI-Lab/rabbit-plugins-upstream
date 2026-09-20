## Description:

Generates Xiaohongshu-style viral title candidates from a user's topic or product input by analyzing recent popular note-title patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, brand operators, e-commerce teams, and content strategists use this skill to turn a product, topic, or broad content direction into 10 Xiaohongshu title candidates with match scores, reference links, and rationale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ordinary creative prompts and keyword queries to the external RedFox service.

Mitigation: Review before installing if this external query flow is not acceptable, and avoid entering sensitive topics or private business plans unless you intend them to be queried externally.

Risk: The skill requires a REDFOX_API_KEY for RedFox access.

Mitigation: Use a scoped, revocable key and confirm the key source, scope, expiry, and reset process before use.

Risk: The helper script can write generated Markdown report files locally.

Mitigation: Run it from the intended working directory or set an explicit output path, then review where generated report files are stored.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentforge-cyber/skills/xhs-title-copywriter)
- [RedFoxHub API key setup](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFoxHub](https://redfox.hk)
- [Xiaohongshu note reference URL pattern](https://www.xiaohongshu.com/explore/{photoId})
- [README.en.md](artifact/README.en.md)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [fetch_xhs_trends.py](artifact/scripts/fetch_xhs_trends.py)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain-language recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 10 title candidates with match scores, reference links, and rationale; the helper script may write a keyword-specific Markdown data report.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
