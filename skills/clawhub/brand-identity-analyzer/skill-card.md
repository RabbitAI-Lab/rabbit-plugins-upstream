## Description: <br>
Generates structured brand identity profiles by researching a brand with Gemini and Google Search grounding, then returning a reusable JSON profile for creative workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pauldelavallaz](https://clawhub.ai/user/pauldelavallaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creative workflow operators use this skill to create or refresh brand identity JSON profiles for ad generation and related creative pipelines. The skill is useful when a brand is missing from an existing catalog or needs an updated profile. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Brand names and prompts are sent to Gemini and Google Search during analysis. <br>
Mitigation: Use only when sharing the target brand information with Gemini and Google Search is acceptable for the deployment context. <br>
Risk: Generated brand profiles may be saved for reuse in downstream creative workflows. <br>
Mitigation: Review generated JSON before reuse and store profiles only in approved project locations. <br>
Risk: The artifact instructs users to push generated brand profiles to GitHub after creation. <br>
Mitigation: Require manual approval before any git commit or push, confirm the target repository and branch, and avoid automatic pushes to main. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pauldelavallaz/skills/brand-identity-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [JSON brand identity profile, optionally saved to a file, with shell commands and operational guidance in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Gemini API key; generated profiles may be printed to stdout, written to a chosen path, or saved to an Ad-Ready brand catalog.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
