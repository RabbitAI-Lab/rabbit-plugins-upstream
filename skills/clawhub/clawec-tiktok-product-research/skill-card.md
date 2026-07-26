## Description: <br>
Uses the ClawEC API to analyze TikTok Shop category product opportunities, including sales rankings, lifecycle stage, entry-window signals, creator and video trends, and optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce sellers, operators, and agents use this skill to submit TikTok Shop category research to ClawEC, retrieve result logs and details, and summarize opportunity products and optional AI analysis for product selection decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scripts require a CLAWEC_API_KEY and send product research requests to clawec.com. <br>
Mitigation: Use an environment variable for the key, do not hardcode or commit it, and run the scripts only when the user intends to call ClawEC. <br>
Risk: The logs and detail endpoints can expose the user's ClawEC product research history and analysis details. <br>
Mitigation: Treat returned logs, detail payloads, product lists, and AI analysis as user data; avoid sharing them unless the user explicitly requests it. <br>
Risk: Optional AI interpretation and market metrics may be incomplete, delayed, or unsuitable as the sole basis for commercial product decisions. <br>
Mitigation: Present AI analysis and product opportunity signals as decision support, preserve source metrics, and recommend human review before acting on sourcing or investment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-tiktok-product-research) <br>
- [ClawEC API base](https://www.clawec.com/api) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>
- [TikTok product opportunity search endpoint](https://www.clawec.com/api/aigc/ec/tiktok/product_opportunity/search) <br>
- [TikTok product opportunity logs endpoint](https://www.clawec.com/api/aigc/ec/tiktok/product_opportunity/search/logs) <br>
- [TikTok product opportunity detail endpoint](https://www.clawec.com/api/aigc/ec/tiktok/product_opportunity/search/log/detail) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with JSON API responses and inline bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include TikTok Shop category metrics, ranked product opportunities, entry-window reasoning, creator/video trend notes, and optional AI analysis from ClawEC.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
