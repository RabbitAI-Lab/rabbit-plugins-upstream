## Description: <br>
Evaluates Amazon product categories for market size, competition intensity, brand landscape, pricing structure, and consumer pain points, then returns a GO, CAUTION, or AVOID market-entry recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and ecommerce operators use this skill to evaluate a named product niche or category before deciding whether to enter it. It supports market-entry diligence with ZooData-backed demand, competition, pricing, brand concentration, competitor, review, and trend analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Amazon market keywords, category paths, ASINs, marketplace/date values, and numeric filters to ZooData using the user's API key. <br>
Mitigation: Use the skill only with inputs appropriate for ZooData and avoid adding sensitive business-profile text beyond the required market research inputs. <br>
Risk: ZooData API calls consume account credits, and the composite market-entry workflow can require about 15 to 25 credits. <br>
Mitigation: Estimate credit cost and confirm before broad or ambiguous multi-call scans; use granular commands when operating under a credit cap. <br>
Risk: The review-analysis fallback can create temporary working files under /tmp. <br>
Mitigation: Remove temporary review-analysis files after the workflow completes, especially on shared systems. <br>
Risk: Legacy or unexpected credential sources can affect which ZooData key is used. <br>
Mitigation: Check the environment for ZOODATA_API_KEY and legacy APICLAW_API_KEY before use, and keep only the intended credential configured. <br>


## Reference(s): <br>
- [Market Entry Analyzer API Field Reference](references/reference.md) <br>
- [ZooData API Documentation](https://api.zoodata.ai/api-docs) <br>
- [ZooData](https://zoodata.ai) <br>
- [ZooData-Skills homepage from metadata](https://github.com/SerendipityOneInc/ZooData-Skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with tables, confidence labels, data provenance, API usage, and optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses GO, CAUTION, and AVOID verdicts; output language follows the user's input language.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
