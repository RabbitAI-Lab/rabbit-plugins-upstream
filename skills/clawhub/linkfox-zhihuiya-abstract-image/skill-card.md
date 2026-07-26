## Description: <br>
Retrieves patent abstract drawings from the Zhihuiya patent database by patent ID or publication number and returns image paths with patent metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve and display the abstract drawing for a single patent when they have a patent ID or publication number. It is for lookup and presentation, not patent analysis or legal interpretation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Full API responses and cache files are saved locally, which can retain patent lookup inputs and returned patent data. <br>
Mitigation: Use a dedicated workspace, review generated linkfox data and cache files, and remove stored responses when they are no longer needed. <br>
Risk: Patent identifiers and the LinkFox API key are sent to the configured tool gateway. <br>
Mitigation: Use trusted environment variables, keep API keys scoped and rotated, and verify LINKFOX_TOOL_GATEWAY before running the skill. <br>
Risk: Patent image lookups consume credits and can create unexpected cost if repeated. <br>
Mitigation: Run one patent per request, get explicit user consent before additional lookups, and rely on the 24-hour cache for repeated parameters. <br>
Risk: Authentication or credit failures may lead to onboarding flows that request installation of an additional LinkFox skill. <br>
Mitigation: Review and approve any download or installation request before allowing the onboarding dependency. <br>
Risk: Automatic feedback reporting may transmit task context to a separate feedback endpoint. <br>
Mitigation: Confirm feedback content is necessary and does not include sensitive patent or workspace details before reporting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-abstract-image) <br>
- [Publisher profile](https://clawhub.ai/user/linkfox-ai) <br>
- [Zhihuiya abstract image API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance] <br>
**Output Format:** [Markdown with inline image links, JSON API responses, and saved JSON data files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts one patent ID or one publication number per request; saves the full response locally, summarizes responses above 8 KB unless inline output is requested, and uses a 24-hour local cache for repeated parameters.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
