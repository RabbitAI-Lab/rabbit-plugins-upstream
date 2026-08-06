## Description: <br>
Turns video links, video files, and key frames into source-grounded editable short-video posters, typography systems, memory journals, audits, and provenance-aware handoff data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legithubhh](https://clawhub.ai/user/legithubhh) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
External creators, designers, editors, and developers use this skill to turn supplied videos or key frames into evidence-backed posters, cover art, editable memory journals, typography plans, and reviewable production handoffs. It is also used to audit factual fidelity, text integrity, thumbnail readability, provenance, and privacy-bounded optimization packs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes supplied videos, frames, references, and journal metadata for creative output. <br>
Mitigation: Use only media and metadata the user is comfortable providing to the agent, and preserve the skill's source records, evidence IDs, and provenance fields in handoffs. <br>
Risk: Optimization inputs could expose raw prompts, media links, identifiers, IPs, credentials, or personal content if prepared carelessly. <br>
Mitigation: Use the optimization branch only with aggregate, privacy-safe packs and exclude raw prompts, media, links, identifiers, IPs, credentials, and personal content from telemetry inputs. <br>
Risk: Generated posters and journals can still contain factual, text, thumbnail, or provenance errors even after automated checks. <br>
Mitigation: Review the final rendered poster or journal before publication and treat the skill's audit as a gate that can block or request repair, not as a guarantee that the work is ready to ship. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legithubhh/skills/shiguang-memory-journal) <br>
- [Evidence-Grounded Video Poster Workflow](references/video-poster-workflow.md) <br>
- [Poster Typography Director](references/poster-typography.md) <br>
- [Workflow playbook](references/workflow-playbook.md) <br>
- [Portable data contracts](references/data-contracts.md) <br>
- [Tool-agnostic prompt pack](references/prompt-pack.md) <br>
- [Journal style profiles](references/style-profiles.md) <br>
- [Usage-evidence optimization workflow](references/usage-optimization.md) <br>
- [Product principles](references/product-principles.md) <br>
- [Typography plan example](references/typography-plan.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with structured JSON-style handoff data and optional editable poster or journal files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns source records, narrative briefs, concept comparisons, key-art and typography briefs, editable poster or journal specifications, audit results, warnings, blockers, and provenance.] <br>

## Skill Version(s): <br>
2.6.0 (source: release metadata, README, SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
