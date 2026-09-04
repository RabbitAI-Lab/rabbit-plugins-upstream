## Description:

Helps AI-agent users, skill authors, maintainers, and teams turn demand for Humanizer-style productivity workflows into practical checklists, workflows, analyses, code changes, and implementation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External agent users, skill authors, maintainers, and teams use this skill to turn a broad Humanizer-style productivity need into concrete workflows, checklists, implementation support, and validation notes. It is aimed at local-hardware-friendly planning, writing, editing, reviewing, bug-fix, setup-hardening, and reliability tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill allows implicit invocation and uses broad writing, editing, reviewing, and bug-fix triggers, so it may shape unrelated agent tasks without clear user intent.

Mitigation: Review trigger routing before installation and disable implicit invocation if precise skill activation is required.

Risk: The security verdict is suspicious because the skill is broadly scoped, even though the evidence does not identify malware-like behavior.

Mitigation: Review generated guidance before acting on it and scan any adapted skill or workflow before deployment.

## Reference(s):

- [Requirement plan](references/requirement-plan.md)
- [ClawHub Humanizer skill demand signal](https://clawhub.ai/skills/humanizer)
- [ClawHub Nano Banana Pro skill demand signal](https://clawhub.ai/skills/nano-banana-pro)
- [SegmentFault HarmonyOS developer community signal](https://segmentfault.com/brand/harmonyos-next)
- [SegmentFault JavaScript topic signal](https://segmentfault.com/t/javascript)
- [SegmentFault TypeScript topic signal](https://segmentfault.com/t/typescript)
- [ONES research management signal](https://ones.cn/?utm_term=ONES%C2%A0%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86&utm_campaign=%E9%A6%96%E9%A1%B5%E6%A0%87%E7%AD%BE&_channel_track_key=myqX1C0f&utm_source=%E6%80%9D%E5%90%A6%E8%BD%AC%20ONES)
- [SegmentFault remove dashes answer signal](https://segmentfault.com/q/1010000042899333/a-1020000042899335)
- [SegmentFault Android floating window removal signal](https://segmentfault.com/q/1010000004947270)
- [SegmentFault floating window destroy removal signal](https://segmentfault.com/q/1010000004951062)
- [GitHub trending issue signal from star-observatory](https://github.com/FunnymeowwooV0/star-observatory/issues/53)
- [GitHub trending issue signal from news-daily](https://github.com/onysakura/news-daily/issues/7670)
- [GitHub daily issue signal from github-daily](https://github.com/skipmaple/github-daily/issues/1331)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code blocks, shell commands, checklists, configuration snippets, assumptions, validation notes, and follow-up risks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No fixed post-processing requirement; outputs should be tailored to the user's request and checked against stated success criteria.]

## Skill Version(s):

0.20260904.60001 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
