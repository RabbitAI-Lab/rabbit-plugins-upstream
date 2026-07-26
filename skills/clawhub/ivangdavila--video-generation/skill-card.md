## Description: <br>
Create AI videos with Sora 2, Veo 3, Seedance, Runway, and modern APIs using reliable prompt and rendering workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, creators, and production teams use this skill to choose AI video providers, write motion prompts, and build async generation workflows with model routing and fallback guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, rendering parameters, and optional reference media may be sent to third-party AI video providers. <br>
Mitigation: Use only providers approved for the content, avoid sending sensitive media unless the provider is trusted, and choose the local open-source workflow when external upload is not acceptable. <br>
Risk: Local memory or history files may retain project preferences, prompts, costs, or output notes. <br>
Mitigation: Avoid saving sensitive details in ~/video-generation/memory.md or history.md, and review or delete those files periodically. <br>
Risk: Long renders, retries, and premium model rerenders can consume provider credits quickly. <br>
Mitigation: Draft short clips first, use lower-cost tiers for validation, and set spend limits on provider accounts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/video-generation) <br>
- [Skill manifest](artifact/SKILL.md) <br>
- [Model snapshot](artifact/benchmarks.md) <br>
- [Async API patterns](artifact/api-patterns.md) <br>
- [Setup guide](artifact/setup.md) <br>
- [Open-source local video models](artifact/open-source-video.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend third-party provider API calls, model IDs, local memory files, and fallback routing.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
