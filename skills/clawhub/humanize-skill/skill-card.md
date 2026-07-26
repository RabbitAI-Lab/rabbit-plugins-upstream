## Description: <br>
Rewrite AI-looking drafts in the user's voice, using local samples when available, audience/cognition analysis when useful, then check factual claims against evidence before finalizing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fendouai](https://clawhub.ai/user/fendouai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, writers, and teams use this agent skill to revise rough or AI-looking drafts into clearer, more specific, voice-aware text. It can also support audience analysis, voice profiling from user-selected samples, and factual claim checks before publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process private writing samples, local files, or account exports when the user selects them for voice matching. <br>
Mitigation: Use only the minimum samples needed, avoid broad private archives unless necessary, and review what the agent read or summarized before sharing outputs. <br>
Risk: Users may confuse quality-focused editing with a guarantee that AI detectors will not flag the result. <br>
Mitigation: Keep detector-related work opt-in, do not promise detector outcomes, and frame results as improved clarity, voice, specificity, and factual grounding. <br>
Risk: Rewrites of product, health, technical, legal, financial, or public-facing text can preserve unsupported claims if evidence is incomplete. <br>
Mitigation: Run the fact-check pass, soften or remove unsupported claims, and keep a concise evidence note when factual claims affect publication risk. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/fendouai/skills/humanize-skill) <br>
- [Lynote.ai](https://lynote.ai) <br>
- [Anti-AI patterns](docs/anti-ai-patterns.md) <br>
- [Audience, cognition, and author persona](docs/audience-persona.md) <br>
- [Fact-check](docs/fact-check.md) <br>
- [Specificity and thought visibility](docs/specificity-and-thought.md) <br>
- [Voice profile: deep matching](docs/voice-profile-deep.md) <br>
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) <br>
- [blader/humanizer](https://github.com/blader/humanizer) <br>
- [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) <br>
- [Oumi HallOumi](https://oumi.ai/blog/introducing-halloumi-a-state-of-the) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or plain text rewrites with optional editorial notes, evidence status, and concise quality reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use user-selected writing samples, local files, exports, or provided evidence when the user authorizes them.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
