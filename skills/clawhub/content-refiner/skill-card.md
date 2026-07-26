## Description: <br>
Content Refiner rewrites Chinese content for multiple publishing platforms using local rewriting or optional LLM-assisted rewriting, with SimHash similarity checks and change summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content creators, marketers, and publishing teams use this skill to adapt Chinese drafts for platform-specific styles, reduce near-duplicate wording, and review similarity and change details before publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive drafts, proprietary copy, or regulated content may be exposed to a configured model provider when LLM mode is enabled. <br>
Mitigation: Use local mode for sensitive material, or route LLM mode only through an approved provider and data-handling policy. <br>
Risk: The skill requests command execution for a text-focused workflow, including troubleshooting commands such as ping. <br>
Mitigation: Install it only in an agent profile with limited command execution and review command requests before allowing them. <br>
Risk: Rewriting content to reduce similarity can create copyright, platform-policy, or disclosure risk if used to disguise copied material. <br>
Mitigation: Require users to verify rights to source material and review rewritten output for accuracy, attribution, and compliance before publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/content-refiner) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON objects and concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include original and rewritten text, platform, rewrite mode, originality score, SimHash distance, change summary, error state, and status code when available.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
