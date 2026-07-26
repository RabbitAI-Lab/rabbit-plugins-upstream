## Description: <br>
Analyze brands to generate comprehensive brand identity profiles (JSON). Use when the user wants to analyze a brand, create a brand profile, or needs brand data for ad generation. Stores profiles for reuse across Ad-Ready, Morpheus, and other creative workflows. Can list existing profiles and update them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pauldelavallaz](https://clawhub.ai/user/pauldelavallaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creative workflow operators use this skill to research a brand and generate a structured brand identity profile for ad generation, campaign planning, and related creative pipelines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Brand-analysis prompts and research requests are sent to Google/Gemini. <br>
Mitigation: Install and run the skill only when that external API use is acceptable for the brand information being analyzed. <br>
Risk: Generated brand profiles can be written to the Ad-Ready catalog or another filesystem path. <br>
Mitigation: Prefer stdout or a deliberate project-local output path first, and use auto-save only when the generated profile should be added to the catalog. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/pauldelavallaz/skills/ai-brand-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON brand profile, with usage guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Gemini API key. Can write the generated profile to stdout, a user-provided output path, or the Ad-Ready brand catalog when auto-save is selected.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
