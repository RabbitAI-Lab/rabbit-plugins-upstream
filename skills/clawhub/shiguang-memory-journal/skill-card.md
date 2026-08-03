## Description: <br>
Turns video links or files into source-grounded, editable short-video posters and turns key frames or stories into memory journals with evidence, typography, audit, and provenance outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legithubhh](https://clawhub.ai/user/legithubhh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, editors, and agents use this skill to convert source videos, key frames, and user stories into editable posters, short-video covers, campaign visuals, and memory journals. It is also used to review factual fidelity, text integrity, reference separation, thumbnail readability, and provenance before release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may require videos, images, source links, archive records, or journal material that can include sensitive personal media. <br>
Mitigation: Provide only media and links needed for the requested poster or journal, keep source ledgers explicit, and avoid sharing raw personal media or identifiers in analytics packs. <br>
Risk: Usage optimization can expose private behavior if raw prompts, media, links, IP addresses, names, emails, or request bodies are handed to the agent. <br>
Mitigation: Use the aggregate, privacy-bounded optimization pack described by the skill and keep raw events, personal content, and identifiers out of agent inputs. <br>
Risk: Poster copy, visual claims, or memory-journal captions can become misleading if the agent invents facts or treats unverified OCR, subtitles, or model commentary as authoritative. <br>
Mitigation: Require every claim to trace to source records or user-provided story evidence, mark unavailable provenance explicitly, and return blockers when evidence is missing. <br>
Risk: Reference posters can cause unwanted content, brand, text, or factual transfer into the new work. <br>
Mitigation: Use references only for layout, hierarchy, relative scale, text-image relationship, spacing, abstract color, and material language; audit final outputs for reference leakage. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/legithubhh/skills/shiguang-memory-journal) <br>
- [README](README.md) <br>
- [Evidence-Grounded Video Poster Workflow](references/video-poster-workflow.md) <br>
- [Poster Typography Director](references/poster-typography.md) <br>
- [Workflow Playbook](references/workflow-playbook.md) <br>
- [Product Principles](references/product-principles.md) <br>
- [Journal Style Profiles](references/style-profiles.md) <br>
- [Tool-Agnostic Prompt Pack](references/prompt-pack.md) <br>
- [Portable Data Contracts](references/data-contracts.md) <br>
- [Usage-Evidence Optimization Workflow](references/usage-optimization.md) <br>
- [Typography Plan Example](references/typography-plan.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance and structured JSON handoff records, with optional editable poster or journal project files and rendered previews] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs keep stable source IDs, provenance, warnings, blockers, audit status, typography plans, and privacy-bounded optimization evidence.] <br>

## Skill Version(s): <br>
2.5.0 (source: ClawHub release metadata, README, SKILL.md, test-prompts.json, and package-local version evolution) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
