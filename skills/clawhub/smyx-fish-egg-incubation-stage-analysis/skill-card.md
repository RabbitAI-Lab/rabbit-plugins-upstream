## Description: <br>
Through breeding-tank fixed cameras or macro-lens inputs, this skill analyzes fish-egg images or videos to identify incubation stages, report visual development signals, and provide breeding-stage recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ornamental fish breeders, aquaculture hatchery staff, and laboratory users can use this skill to classify fish-egg incubation stages from macro images or videos, monitor eye-spot and color-change signals, and receive structured guidance about likely hatching progress. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fish-egg images, videos, or media URLs may be sent to the publisher's cloud service for analysis. <br>
Mitigation: Use the skill only with media the user is comfortable uploading, and review the publisher's retention and account-linkage expectations before deployment. <br>
Risk: The security scan reports silent local identity linking and local bearer-token storage. <br>
Mitigation: Run the skill in an isolated environment, inspect local credential storage, and remove or rotate stored tokens when access is no longer needed. <br>
Risk: History lookup may fetch prior reports through the local identity associated with the skill. <br>
Mitigation: Avoid shared workstations for report lookup and confirm that historical report access matches the user's authorization and privacy expectations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-egg-incubation-stage-analysis) <br>
- [Fish egg incubation API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summaries with JSON-capable structured report fields and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include incubation-stage classifications, color distribution metrics, eye-spot detection ratios, recommended actions, disclaimers, report links, and history tables.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
